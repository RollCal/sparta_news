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
    # 게시글 등록,수정,삭제
    path('post/', views.sparta_news_list, name='sparta_news_list'),
    path('create/', views.sparta_news_create, name='sparta_news_create'),
    path('<int:pk>/', views.sparta_news_detail, name='sparta_news_detail'),
    path('<int:pk>/update/', views.sparta_news_update, name='sparta_news_update'),
    path('<int:pk>/delete/', views.sparta_news_delete, name='sparta_news_delete'),
]
