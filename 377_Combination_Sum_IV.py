"""
377. Combination Sum IV
Medium
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""
from typing import List
from unittest import TestCase

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        num_ways = [0 for idx in range(target+1)]
        num_ways[0] = 1
        for idx in range(1, target+1):
            for num in nums:
                if num > idx: continue
                num_ways[idx] += num_ways[idx-num]
        return num_ways[-1]
    # num_ways[current_sum] = num_ways[i] + num_ways[j] where i + k == current sum

class TestSolution(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()
        self.testcases = [
            ([1,2,3], 4, 7),
            ([9], 3, 0)
        ]
        
    def test_combinationSum4(self):
        for nums, target, expected in self.testcases:
            self.assertEqual(self.solution.combinationSum4(nums, target), expected)
  
  
if __name__ == '__main__':
    test = TestSolution()
    test.test_combinationSum4()
    print('All Passed!')