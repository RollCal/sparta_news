from rest_framework import generics
from rest_framework.response import Response

from rest_framework import status, generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import spartanews
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, Http404
from .models import Comment
from .serializers import CommentSerializer, PostSerializer
from accounts.models import User

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


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]  # 인증된 사용자만 댓글 작성 가능하도록 설정

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('pk')
        serializer.save(user=self.request.user, post_id=post_pk)

