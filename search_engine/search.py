import numpy as np
from post.models import spartanews
from sparta_news.embedding import get_embedding


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

    for document in spartanews.objects.all():
        document_embedding = get_embedding(document.get_text_representation())
        similarity = cosine_similarity(query_embedding, document_embedding)

        if similarity >= threshold:
            relevant_results.append(document)

    return relevant_results

