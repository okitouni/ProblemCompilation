# 1347. Minimum Number of Steps to Make Two Strings Anagram
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        total = 0
        for char in counter_s:
            total += max(counter_s[char] - counter_t[char], 0)

        return total
