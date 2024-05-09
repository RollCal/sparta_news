from rest_framework import serializers

from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source='content')  # 'content' 필드를 'text' 필드로 사용

    class Meta:
        model = Document
        fields = ('id', 'text', 'embedding')

