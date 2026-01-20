from app.embeddings.embedder import embed
from app.embeddings.vector_store import add
text='Sample memory'; add(embed(text),text); print('Indexed')
