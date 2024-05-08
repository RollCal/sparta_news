from django.db import models
from post.models import spartanews, Comment  # spartanews와 Comment 모델 import
from sparta_news.embedding import get_embedding

class Document(models.Model):
    text = models.TextField()
    embedding = models.BinaryField(null=True, blank=True) #임베딩 저장 필드

    def save(self, *args, **kwargs):
        # 문서의 텍스트 생성
        spartanews_text = '\n'.join(
            spartanews_obj.get_text_representation() for spartanews_obj in spartanews.objects.all())
        comment_text = '\n'.join(comment_obj.content for comment_obj in Comment.objects.all())
        self.text = f"{spartanews_text}\n{comment_text}"

        # 임베딩 생성
        embedding = get_embedding(self.text)

        # 임베딩 저장
        self.embedding = embedding.tobytes() if embedding is not None else None

        super().save(*args, **kwargs)
