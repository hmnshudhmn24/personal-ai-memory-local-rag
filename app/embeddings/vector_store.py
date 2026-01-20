import faiss, numpy as np
index=faiss.IndexFlatL2(128); texts=[]
def add(v,t): index.add(np.array([v])); texts.append(t)
def search(v,k=3): D,I=index.search(np.array([v]),k); return [texts[i] for i in I[0]]
