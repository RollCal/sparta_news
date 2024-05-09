from rest_framework import generics
from post.models import spartanews
from .serializers import DocumentSerializer
from . import search
from rest_framework.response import Response
from django.http import JsonResponse
from elasticsearch_dsl import Search
from django.views import View


class SearchDocumentView(View):
    def get(self, request):
        query = request.GET.get('query')

        # Elasticsearch에서 검색 쿼리 생성
        s = Search(index='spartanews-index')

        # 제목과 내용에 대한 검색 쿼리 설정
        s = s.query('multi_match', query=query, fields=['title', 'content'])

        # Elasticsearch에서 검색 실행
        response = s.execute()

        # 검색 결과 처리
        relevant_results = []
        for hit in response:
            relevant_results.append(hit)

        # 검색 결과를 직렬화하여 JSON 형태로 반환
        serializer = DocumentSerializer(relevant_results, many=True)
        return JsonResponse({'results': serializer.data})
