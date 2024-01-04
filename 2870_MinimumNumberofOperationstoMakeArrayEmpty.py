# 2870. Minimum Number of Operations to Make Array Empty
# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.


from typing import List
from collections import Counter
from functools import cache
import math
from unittest import TestCase, main

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp =Counter(nums)
        res =0 
        for v in mp.values():
            if v==1:return -1 
            res +=math.ceil(v/3) 
        return res 


class StupidSolution:
    def minOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(count):
            if count <= 1:
                return float('inf')
            elif count == 2 or count == 3:
                return 1
            return min(dfs(count-2), dfs(count-3)) + 1
        counter = Counter(nums)
        result = 0
        for value_count in counter.values():
            result += dfs(value_count)
        if result == float('inf'):
            return -1
        return result

        
        
class TestSolutions(TestCase):
    def setUp(self) -> None:
        self.cases = [
            [1,1,1],
            [19] * 13,
            [1,2,2,2,3,4,4,4,4,4,4,4,4,4,4,4],
        ]
        self.answers = [
            1,
            5,
            -1,
        ]
        
    def test_stupid(self):
        for case, answer in zip(self.cases, self.answers):
            self.assertEqual(answer, StupidSolution().minOperations(case))
    def test_solution(self):
        for case, answer in zip(self.cases, self.answers):
            self.assertEqual(answer, Solution().minOperations(case))
        
        
if __name__ == "__main__":
    main()
    
