import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

vetor1 = np.array([2, 5])
vetor2 = np.array([9, 8])

print(cosine_similarity([vetor1], [vetor2]))
