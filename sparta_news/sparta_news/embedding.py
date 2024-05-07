import spacy


def get_embedding(text):
    # spaCy 또는 Gensim과 같은 적절한 라이브러리를 사용하여 임베딩 함수 구현
    nlp = spacy.load('en_core_web_sm')

    # 텍스트 처리 -> 문서 객체 생성
    doc = nlp(text)

    # 문서 객체의 벡터 변환
    return doc.vector
