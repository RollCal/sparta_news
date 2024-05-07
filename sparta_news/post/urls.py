from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    # 게시글 등록,수정,삭제
    path('', views.sparta_news_list, name='sparta_news_list'),
    path('create/', views.sparta_news_create, name='sparta_news_create'),
    path('<int:pk>/', views.sparta_news_detail, name='sparta_news_detail'),
    path('<int:pk>/update/', views.sparta_news_update, name='sparta_news_update'),
    path('<int:pk>/delete/', views.sparta_news_delete, name='sparta_news_delete'),
]
