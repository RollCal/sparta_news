from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from post.models import Comment

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['first_name','last_login',"is_superuser",'last_name','is_staff','is_active','date_joined','groups','user_permissions']

class UserSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'comments']

class LikedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']
