# 645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0]* len(nums)
        for num in nums:
            counts[num-1] += 1
        result = [0, 0]
        for idx, count in enumerate(counts):
            if count == 0:
                result[1] = idx + 1
            elif count == 2:
                result[0] = idx + 1
            else:
                continue
        return result
        