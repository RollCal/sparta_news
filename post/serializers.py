from rest_framework import serializers
from .models import spartanews
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = spartanews
        fields = ['id', 'title', 'content', 'created_at', 'liked_by']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'liked_by']
        read_only_fields = ['post', 'user']
