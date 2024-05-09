from .models import spartanews
from datetime import datetime

def update_news_point():
    now = datetime.now()
    print('포인트가 차감되었습니다. 차감된 시각:', now)
    posts = spartanews.objects.all()
    for post in posts:
        post.point -= 5 
        post.save()