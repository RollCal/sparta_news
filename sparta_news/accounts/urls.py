from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


urlpatterns = [
    # 회원가입
    path('', views.AccountListAPIView.as_view()),
    # 로그인
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('comment_list/liked/', views.LikedCommentListView.as_view(), name='comments_liked'),
    path('comment_list/saved/', views.SavedCommentListView.as_view(), name='comments_saved'),
    path('post_list/liked/', views.LikedPostListView.as_view(), name='Posts_liked'),
    path('post_list/saved/', views.SavedPostListView.as_view(), name='Posts_saved'),
]

