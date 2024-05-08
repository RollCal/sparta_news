from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .models import spartanews, Comment
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, Http404
from .serializers import CommentSerializer, PostSerializer
from accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class SpartaNewsList(generics.ListCreateAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SpartaNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = spartanews.objects.all()
    serializer_class = PostSerializer

class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 댓글의 게시물 ID는 URL에서 가져옵니다.
        post_id = self.kwargs['pk']
        post = get_object_or_404(spartanews, pk=post_id)
        serializer.save(user=self.request.user, post=post)
class UpdateCommentView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
