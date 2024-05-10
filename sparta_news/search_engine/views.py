from rest_framework import generics
from .models import Document
from post.models import spartanews
from .serializers import DocumentSerializer
from . import search
from rest_framework.response import Response
from django.db.models import Q


class SearchDocumentView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer

    def retrieve(self, request, pk=None):
        검색어 = request.GET.get('query')

        # search.py 파일에서 search 함수를 사용하여 검색 수행
        검색결과 = search.search(검색어)

        # 검색 결과가 실제 검색어와 관련이 있는지 확인하여 필터링
        관련있는_검색결과 = [item for item in 검색결과 if 검색어 in item.content or 검색어 in item.title]
# 튜터님 팁: 리스트, 튜플 대조 -> 검색어와 유사도
        # 검색 결과를 SpartanNews 객체의 ID로 변환
        관련있는_검색결과_ids = [item.id for item in 관련있는_검색결과]

        # 검색 결과(ID) 기반으로 SpartanNews 객체 필터링
        해당_문서들 = spartanews.objects.filter(id__in=관련있는_검색결과_ids)

        # 검색된 문서만 직렬화
        직렬화된_데이터 = self.serializer_class(해당_문서들, many=True).data

        return Response({
            'results': 직렬화된_데이터
        })
