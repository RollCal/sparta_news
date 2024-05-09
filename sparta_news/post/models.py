from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model
from sparta_news.embedding import get_embedding


class spartanews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    embedding = models.BinaryField(null=True, blank=True)
    liked_by = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)
    def get_text_representation(self):
        return f"{self.title} {self.content}"
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.liked_by.count()

    def save(self, *args, **kwargs):
        # 임베딩 생성 및 저장
        if not self.embedding or self.embedding is None:  # 임베딩이 없거나 None인 경우에만 생성 및 저장
            # 임베딩 생성 및 저장
            embedding = get_embedding(self.get_text_representation())
            self.embedding = embedding.tobytes()

        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(spartanews, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    embedding = models.BinaryField(null=True, blank=True)
    liked_by = models.ManyToManyField(get_user_model(), related_name='liked_comments', blank=True)
    def __str__(self):
        return f'{self.user.username}님의 {self.post.title}에 대한 댓글'

    def total_likes(self):
        return self.liked_by.count()
    def save(self, *args, **kwargs):
        if not self.embedding:  # 임베딩이 이미 저장되어 있지 않은 경우에만 생성 및 저장
            # 임베딩 생성 및 저장
            embedding = get_embedding(self.content)
            self.embedding = embedding.tobytes()

        super().save(*args, **kwargs)
