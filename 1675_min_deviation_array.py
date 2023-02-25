# 1675_min_deviation_array.py
# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.
from typing import List
import heapq

def min_deviation(nums: List[int]) -> int:
    q = [-num<<1 if num&1 else -num for num in nums]
    heapq.heapify(q)
    smallest = -max(q)
    ans = float('inf')
    while q[0] & 1 == 0:
        ans = min(ans, -q[0] - smallest)
        smallest = min(smallest, -q[0]//2)
        heapq.heappush(q, heapq.heappop(q)//2)
    return min(ans, -q[0] - smallest)

nums = [4,1,5,20,3]
print(min_deviation(nums))