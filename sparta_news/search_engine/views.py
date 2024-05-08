from rest_framework import generics

from .models import Document
from post.models import spartanews
from .serializers import DocumentSerializer
from . import search
from rest_framework.response import Response
from django.db.models import Q


class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class SearchDocumentView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer

    def retrieve(self, request, pk=None):
        검색어 = request.GET.get('query')

        # search.py 파일에서 search 함수를 사용하여 검색 수행
        검색결과 = search.search(검색어)

        # 검색 결과(content)가 포함된 SpartanNews 객체 필터링
        # 부분 문자열을 포함하는 경우를 처리하기 위해 Q 객체를 사용합니다.
        해당_문서 = spartanews.objects.filter(
            Q(content__contains=검색어) |
            Q(title__contains=검색어)
        )

        # 필터링된 문서 직렬화
        직렬화된_데이터 = self.get_serializer(해당_문서, many=True).data

        return Response({
            'results': 직렬화된_데이터
        })
