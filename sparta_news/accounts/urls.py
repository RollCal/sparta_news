from django.urls import path, include
from . import views

urlpatterns = [
    #회원가입
    path('',views.AccountListAPIView.as_view()),
]
