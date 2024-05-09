import numpy as np
from post.models import spartanews
from sparta_news.embedding import get_embedding
from django.db.models import Q


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity


def search(query):
    query_embedding = get_embedding(query)
    threshold = 0.5  # 임계값 설정 (실험적으로 조정 필요)

    relevant_results = []

    # 검색 쿼리를 포함하는 spartanews 객체 필터링
    relevant_documents = spartanews.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    # 필터링된 문서들에 대해서만 처리
    for document in relevant_documents:
        # 각 문서의 제목과 내용을 개별적으로 임베딩 생성
        title_embedding = get_embedding(document.title)
        content_embedding = get_embedding(document.content)

        # 제목과 내용의 임베딩을 합침
        document_embedding = (title_embedding + content_embedding) / 2

        similarity = cosine_similarity(query_embedding, document_embedding)

        if similarity >= threshold:
            relevant_results.append(document)

    return relevant_results

