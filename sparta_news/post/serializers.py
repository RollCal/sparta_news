from rest_framework import serializers
from .models import spartanews
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = spartanews
        fields = ['id', 'title', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['post', 'user']

class CommentdetailSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'total_likes']  # 'total_likes' 필드 추가
        read_only_fields = ['post', 'user']

    def get_total_likes(self, obj):
        return obj.total_likes()  # 댓글에 대한 좋아요를 누른 사용자의 총 수를 반환하는 메서드

class PostdetailSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = spartanews
        fields = ['id', 'content', 'created_at', 'total_likes']  # 'total_likes' 필드 추가
        read_only_fields = ['post', 'user']

    def get_total_likes(self, obj):
        return obj.total_likes()  # 게시물에 대한 좋아요를 누른 사용자의 총 수를 반환하는 메서드
