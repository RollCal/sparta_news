from .serializers import DocumentSerializer
from django.http import JsonResponse
from elasticsearch_dsl import Search
from django.views import View
from elasticsearch import Elasticsearch

def search(request):
    # Elasticsearch 클라이언트 설정
    es = Elasticsearch(['localhost:8000'])  # Elasticsearch 호스트와 포트

    # Elasticsearch 쿼리 실행
    query = request.GET.get('query', '')  # URL에서 쿼리 가져오기
    results = es.search(index='spartanews-index', body={'query': {'match': {'content': query}}})

    # 결과 처리
    hits = results['hits']['hits']
    search_results = [hit['_source'] for hit in hits]

    # JSON 형식으로 결과 반환
    return JsonResponse({'results': search_results})
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

