from .models import spartanews

def update_news_point():
    print('포인트가 차감되었습니다')
    posts = spartanews.objects.all()
    for post in posts:
        post.point -= 5 
        post.save()