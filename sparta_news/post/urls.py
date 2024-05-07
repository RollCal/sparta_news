from django.urls import path
from . import views

urlpatterns = [
    path('', views.SpartaNewsList.as_view(), name='sparta_news_list'),
    path('<int:pk>/', views.SpartaNewsDetail.as_view(), name='sparta_news_detail'),
]
