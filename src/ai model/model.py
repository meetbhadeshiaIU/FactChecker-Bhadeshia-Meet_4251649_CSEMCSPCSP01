from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-mpnet-base-v2')


def check_similarity_score(news1: str, news2: str) -> float:
    emb1 = model.encode(news1, convert_to_tensor=True)
    emb2 = model.encode(news2, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2)
    return int(similarity*100) 