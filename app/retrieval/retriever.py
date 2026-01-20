from app.embeddings.embedder import embed
from app.embeddings.vector_store import search

def retrieve(q): return search(embed(q))
