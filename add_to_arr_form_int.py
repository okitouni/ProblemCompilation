# Add to Array-Form of Integer
# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
# %%
from typing import List
from timeit import timeit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np

def to_arr(num: int) -> List[int]:
    if num == 0:
        return [0]
    arr = []
    while num:
        arr.append(num % 10)
        num //= 10
    return arr[::-1]


def to_int(arr: List[int]) -> int:
    num = 0
    for element in arr:
        num *= 10
        num += element
    return num


def add(num: List[int], k: int) -> List[int]:
    return to_arr(to_int(num)+k)

times = []
n = list(range(0, 1000, 10))
for i in n:
    arr = [1]*i
    times.append(timeit("add(arr, 34)", globals=globals(), number=100))
# %%
# test linear relationship
n , times = np.array(n).reshape(-1, 1), np.array(times).reshape(-1, 1)

sol = LinearRegression().fit(n, times)
print("R2", sol.score(n, times))
plt.scatter(n, times)
plt.plot(n, sol.predict(n), 'r', label='fitted line')
plt.show()

# %%
# test quadratic relationship
n = np.array(n)
x = np.hstack([n, n**2])
sol = LinearRegression().fit(x, times)
print("R2", sol.score(x, times))
plt.scatter(n, times)
plt.plot(n, sol.predict(x), 'r', label='fitted line')
# %%
