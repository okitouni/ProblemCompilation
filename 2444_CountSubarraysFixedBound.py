# 2444. Count Subarrays With Fixed Bounds

# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.
from typing import List
import unittest

def countSubarrays(nums: List[int], minK: int, maxK: int) -> int:
    if minK > maxK: return 0
    leftbound = -1
    minK_idx = -1
    maxK_idx = -1
    count = 0
    for idx, num in enumerate(nums):
        if num >= minK and num <= maxK:
            minK_idx = idx if minK == num else minK_idx
            maxK_idx = idx if maxK == num else maxK_idx
            count += max(0, min(maxK_idx, minK_idx) - leftbound)
        else:
            leftbound = idx
    return count
            

class Test(unittest.TestCase):
    def test_countSubarrays(self):
        self.assertEqual(countSubarrays([2, 3, 3, 4, 3], 2, 3), 2)
        self.assertEqual(countSubarrays([2, 4, 2], 2, 4), 3)
        self.assertEqual(countSubarrays([2, 4, 1, 2], 2, 4), 1)

if __name__ == "__main__":
    unittest.main()