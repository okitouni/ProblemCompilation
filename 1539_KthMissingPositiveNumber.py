# 1539. Kth Missing Positive Number
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.
from typing import List
from unittest import TestCase, main
from bisect import bisect_left
from collections import Counter

def find_k_positive(arr:List[int], k:int) -> int:
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        missing = arr[mid] - mid - 1
        if missing < k:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return lower_bound + k

class TestFindKPositive(TestCase):
    def test_generic(self):
        self.assertEqual(9, find_k_positive([2,3,4,7,11], 5))
        self.assertEqual(6, find_k_positive([1,2,3,4], 2))
        self.assertEqual(9, find_k_positive([1,2,3,4], 5))

if __name__ == "__main__":
    main()
    
