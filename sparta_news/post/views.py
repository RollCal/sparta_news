from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import spartanews, Comment
from .serializers import PostSerializer, CommentSerializer, CommentdetailSerializer, PostdetailSerializer
from django.db.models import Q

class SpartaNewsList(generics.ListCreateAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SpartaNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostdetailSerializer
    permission_classes = [AllowAny]  

    def update(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)

class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = get_object_or_404(spartanews, pk=post_id)
        serializer.save(user=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)

class CommentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentdetailSerializer(comments, many=True)
        return Response(serializer.data)


class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        post = get_object_or_404(spartanews, pk=pk)
        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            return Response({'status': 'unliked'})
        else:
            post.liked_by.add(request.user)
            return Response({'status': 'liked'})

class LikeCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user in comment.liked_by.all():
            comment.liked_by.remove(request.user)
            return Response({'status': 'unliked'})
        else:
            comment.liked_by.add(request.user)
            return Response({'status': 'liked'})

class PostSearchView(generics.ListAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]  # SearchFilter를 사용하여 검색 활성화
    search_fields = ['title', 'content']  # 검색할 필드들을 지정

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        # 검색어가 전달되었는지 확인하고 필터링 수행
        search_term = query_params.get('search', None)
        if search_term:
            # 검색어를 공백으로 분리하여 각 단어를 검색하도록 설정
            search_words = search_term.split()
            # 각 단어를 포함하는지 확인하는 Q 객체 생성
            q_objects = Q()
            for word in search_words:
                q_objects |= Q(title__icontains=word) | Q(content__icontains=word)
            # 필터링 수행
            queryset = queryset.filter(q_objects)
        return queryset
