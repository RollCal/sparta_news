from django.dispatch import receiver
from post.models import Comment, spartanews

from .tasks import process_document

# 새로 생성된 댓글이 처리돼 임베딩 생성, DB에 저장되도록 함.
@receiver(post_save, sender=spartanews)
@receiver(post_save, sender=Comment)  # Comment 모델의 post_save 시그널을 수신합니다.
def process_comment_task(sender, instance=None, created=False, **kwargs):
    # 새로운 댓글이 생성될 때만 작업
    if created:
        # 댓글의 텍스트를 가져와서 임베딩 생성 작업을 비동기적으로 실행.
        process_document.delay(instance.content)
