"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        # fast takes twice as many steps per round
        # if there is a cycle, then x_i = x_{i+n
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast!=slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast