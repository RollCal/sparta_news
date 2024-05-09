from rest_framework import generics
from post.models import spartanews
from .serializers import DocumentSerializer
from . import search
from rest_framework.response import Response


class SearchDocumentView(generics.ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            # search.py 파일에서 search 함수를 사용하여 검색 수행
            search_results = search.search(query)

            # 검색된 문서의 ID 목록 가져오기
            document_ids = [result.id for result in search_results]

            # 해당 문서들 필터링
            queryset = spartanews.objects.filter(id__in=document_ids)
        else:
            queryset = spartanews.objects.none()  # 빈 쿼리셋 반환

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})
