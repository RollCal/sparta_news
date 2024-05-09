from django.urls import path
from . import views


urlpatterns = [
    # 게시글 등록,수정,삭제
    path('', views.SpartaNewsList.as_view(), name='sparta_news_list'),
    path('<int:pk>/', views.SpartaNewsDetail.as_view(), name='sparta_news_detail'),
    path('<int:pk>/comment/', views.CreateCommentView.as_view(), name='sparta_comment'),
    path('<int:pk>/commentlist/', views.CommentListView.as_view(), name='commentlist'),
    path('<int:pk>/like/', views.LikePostAPIView.as_view(), name='like-post'),
    path('<int:pk>/comment/like/', views.LikeCommentAPIView.as_view(), name='like-comment'),
]

