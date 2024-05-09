from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import spartanews, Comment
from .serializers import PostSerializer, CommentSerializer

class SpartaNewsList(generics.ListCreateAPIView):
    queryset = spartanews.objects.all().order_by('-point')
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #생성된 게시글 데이터를 obj에 담는다
        obj = serializer.save()
        # 포인트 추가 후 저장
        obj.point+=5
        obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SpartaNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostSerializer
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
        obj = serializer.save(user=self.request.user, post=post)
        obj.post.point += 3
        obj.post.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateCommentView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class CommentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
