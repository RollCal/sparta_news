from rest_framework import serializers
from .models import spartanews
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = spartanews
        fields = ['id', 'title', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']
