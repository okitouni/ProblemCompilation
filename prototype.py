# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x = np.linspace(0, 1, 100) 
acc1 = x + np.random.normal(0, 0.1, 100)
acc2 = 1.1*x + np.random.normal(0, 0.1, 100) + 0.1
diff = acc2 - acc1
# %%
plt.scatter(x, acc1, label='acc single target')
plt.scatter(x, acc2, label='acc combined target')
plt.legend()
plt.show()
plt.scatter(x, diff, label='diff')
plt.ylabel('acc2 - acc1')
plt.xlabel("training data fraction")
plt.show()
# %%
# get dimension of subspace spanned by a collection of random vectors
dim = 100
n = 49
rand = np.random.randn
v1 = rand(dim, n)
v2 = rand(dim, n)
rank_v1 = np.linalg.matrix_rank(v1)
rank_v2 = np.linalg.matrix_rank(v2)
rank_v1v2 = np.linalg.matrix_rank(np.concatenate((v1, v2), axis=1))
print(f"rank v1: {rank_v1}, rank v2: {rank_v2}, rank v1v2: {rank_v1v2}, overlap: {rank_v1 + rank_v2 - rank_v1v2}")
# get similarity of the spaces spanned by the two collections of vectors
cosine = np.dot(v1.T, v2) / (np.linalg.norm(v1, axis=0) * np.linalg.norm(v2, axis=0))
print(f"cosine similarity: {cosine}")


# %%
from collections import Counter

c = Counter(range(1, 5))
arr = list([2,3,4,7,11])
Counter(range(1, arr[-1]+1)) - Counter(arr) 


# %%
