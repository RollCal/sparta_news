from celery import shared_task
from sparta_news.embedding import get_embedding
from .models import Document


# 새로 생성된 문서의 임베딩을 업데이트하는 로직
@shared_task
def process_document(document_id):
    document = Document.objects.get(id=document_id)
    text = document.text
    embedding = get_embedding(text)
    document.embedding = embedding
    document.save()

