from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    

def generate_embeddings(chunks):
    chunk_texts=[]
    #list compreshension
    # chunk_texts = [chunk["text"] for chunk in chunks]
    for chunk in chunks:
        chunk_texts.append(chunk["text"])
    embeddings=model.encode(chunk_texts)
    return embeddings

def generate_query_embedding(query):
    result=model.encode(query)
    return result