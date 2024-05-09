import spacy

def get_embedding(text):
    # spaCy 또는 Gensim과 같은 적절한 라이브러리를 사용하여 임베딩 함수 구현
    nlp = spacy.load('ko_core_news_sm') # 영어기반 툴 -> 포스트 내용을 영어로 구현했을때 비교적 더 원활한 검색기능구현가능.

    # 텍스트 처리 -> 문서 객체 생성
    doc = nlp(text)
    print(doc.vector.shape)
    # 문서 객체의 벡터 변환(평균 값 사용)
    embedding = doc.vector
    print(embedding.shape)

    if embedding is not None:
        return embedding
    else:
        # 예외 처리: 임베딩이 None인 경우
        raise ValueError("Failed to generate embedding for the text")
embeddings = []
sentences = ["고양이와 산책", "언 맥주", "Take walk with cat"]
for sentence in sentences:
    embedding = get_embedding(sentence)
    embeddings.append(embedding)
target=embeddings[0]
for i in range(1,3):
    dist = (sum((target-embeddings[i])**2))**0.5
    print(dist)
