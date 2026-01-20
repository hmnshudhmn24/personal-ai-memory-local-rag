import numpy as np
def embed(t,dim=128): np.random.seed(len(t)); return np.random.rand(dim).astype('float32')
