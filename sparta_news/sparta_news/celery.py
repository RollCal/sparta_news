from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django 설정을 불러와 Celery 애플리케이션에 등록합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sparta_news.settings')

app = Celery('sparta_news')

# Celery 설정을 로드합니다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery 애플리케이션을 자동으로 발견하고 등록합니다.
app.autodiscover_tasks()
