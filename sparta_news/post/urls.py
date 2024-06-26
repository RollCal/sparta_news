from django.urls import path
from . import views


urlpatterns = [
    # 게시글 등록,수정,삭제
    path('', views.SpartaNewsList.as_view(), name='sparta_news_list'),
    path('<int:pk>/', views.SpartaNewsDetail.as_view(), name='sparta_news_detail'),
    path('<int:pk>/comment/', views.CreateCommentView.as_view(), name='sparta_comment'),
    path('<int:pk>/commentlist/', views.CommentListView.as_view(), name='commentlist'),
    path('<int:pk>/like/', views.LikePostAPIView.as_view(), name='like-post'),
    path('<int:pk>/save/', views.SavePostAPIView.as_view(), name='save-post'),
    path('<int:post_pk>/comment/<int:comment_pk>/like/', views.LikeCommentAPIView.as_view(), name='like-comment'),
    path('<int:post_pk>/comment/<int:comment_pk>/save/', views.SaveCommentAPIView.as_view(), name='save-comment'),
    path('<int:post_pk>/comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('search/', views.PostSearchView.as_view(), name='post-search'),
]
