# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.


from typing import List
from unittest import TestCase, main


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        longest_sequence_ends_with = [1] * n
        for end_num_index in range(n):
            for i in range(end_num_index):
                if nums[i] < nums[end_num_index]:
                    longest_sequence_ends_with[end_num_index] = max(longest_sequence_ends_with[i] + 1, longest_sequence_ends_with[end_num_index])
        return max(longest_sequence_ends_with)
    
    
class TestSolution(TestCase):
    def setUp(self) -> None:
        self.cases = [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
        ]
        
    def test_lengthOfLIS(self) -> None:
        s = Solution()
        for nums, expected in self.cases:
            self.assertEqual(expected, s.lengthOfLIS(nums))
    

if __name__ == '__main__':
    main()