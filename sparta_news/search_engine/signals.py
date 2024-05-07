from django.dispatch import receiver
from .models import Document

from .tasks import process_document

#새로 생성된 문서가 처리돼 임베딩 생성, DB에 저장되도록 함.
@receiver(post_save, sender=Document)
def process_document_task(sender, instance=None, created=False, **kwargs):
    # 새로 문서가 생성될 때만 작업
    if created:
        process_document.delay(instance.id)
