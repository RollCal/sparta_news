from django.urls import path
from .views import SearchDocumentView

urlpatterns = [
    path('search/', SearchDocumentView.as_view(), name='search'),
]
