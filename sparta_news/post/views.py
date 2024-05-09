from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import spartanews, Comment
from .serializers import PostSerializer, CommentSerializer, CommentdetailSerializer, PostdetailSerializer

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
    def post(self, request, post_pk, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user in comment.liked_by.all():
            comment.liked_by.remove(request.user)
            return Response({'status': 'unliked'})
        else:
            comment.liked_by.add(request.user)
            return Response({'status': 'liked'})
