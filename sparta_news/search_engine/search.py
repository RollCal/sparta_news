from .models import Document
from sparta_news.embedding import get_embedding


def search(query):
    embeddings = {document: get_embedding(document.text) for document in Document.objects.all()}
    query_embedding = get_embedding(query)

    similarities = {}
    for document, embedding in embeddings.items():
        similarity = cosine_similarity(query_embedding, embedding)
        similarities[document] = similarity

    ranked_results = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return [document for document, _ in ranked_results]

    pass
