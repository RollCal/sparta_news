from rest_framework import generics

from .models import Document
from .serializers import DocumentSerializer
from . import search
from rest_framework.response import Response

class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

class SearchDocumentView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def retrieve(self, request, pk=None):
        query = request.GET.get('query')
        results = search.search(query)

        return Response({
            'results': [DocumentSerializer(document).data for document in results]
        })
