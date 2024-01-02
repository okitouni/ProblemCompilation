# 2610. Convert an Array Into a 2D Array With Conditions
# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.
from typing import List
from collections import defaultdict
from unittest import TestCase, main

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1

        result = [[] for _ in range(max(num_counts.values()))]

        for num, count in nums.items():
            for idx in range(count):
                result[idx].append(num)
        return result
