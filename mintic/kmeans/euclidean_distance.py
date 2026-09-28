import numpy as np

def euclidean_distance (a, b):
    dim = len(a)
    suma = []
    for d in range(dim):
        suma.append((a[d] - b[d])**2)
    return np.sqrt(sum(suma))
