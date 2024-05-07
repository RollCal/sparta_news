from django.urls import path, re_path
from .views import SearchDocumentView

urlpatterns = [
    path('search/', SearchDocumentView.as_view(), name='search'),
]
