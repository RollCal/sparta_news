from rest_framework import serializers
from .models import spartanews

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = spartanews
        fields = ['id', 'title', 'content', 'created_at']

