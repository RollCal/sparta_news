from django.urls import path
from . import views


urlpatterns = [
    # 게시글 등록,수정,삭제
    path('', views.SpartaNewsList.as_view(), name='sparta_news_list'),
    path('<int:pk>/', views.SpartaNewsDetail.as_view(), name='sparta_news_detail'),
    path('<int:pk>/comment/', views.CommentCreateAPIView.as_view(), name='sparta_comment'),

