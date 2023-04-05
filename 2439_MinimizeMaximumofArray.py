# 2439. Minimize Maximum of Array
# You are given a 0-indexed array nums comprising of n non-negative integers.


# In one operation, you must:

# Choose an integer i such that 1 <= i < n and nums[i] > 0.
# Decrease nums[i] by 1.
# Increase nums[i - 1] by 1.
# Return the minimum possible value of the maximum integer of nums after performing any number of operations.
from math import ceil
from typing import List
import unittest


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prev_max = nums[0]
        slack = 0
        for i in range(1, len(nums)):
            num = nums[i]
            overflow = num - (prev_max + slack)
            if overflow > 0:
                slack = (-overflow) % (i + 1)
                prev_max += ceil((overflow) / (i + 1))
            else:
                slack += prev_max - num
        return prev_max


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        self.cases = [
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 3),
            ([3, 7, 1, 6], 5),
            ([3, 7, 1, 6, 9], 6),
            ([10, 1], 10),
            ([6, 9, 3, 8, 14], 8),
        ]

    def test_minimizeArrayValue(self):
        for case in self.cases:
            self.assertEqual(self.sol.minimizeArrayValue(case[0]), case[1])


if __name__ == "__main__":
    unittest.main()
