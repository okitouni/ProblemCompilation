
# 2405. Optimal Partition of String
# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.
import unittest

class Solution:
    def partitionString(self, s: str) -> int:
        so_far = ""
        num_substrings = 1
        for letter in s:
            if letter not in so_far:
                so_far += letter
            else:
                so_far = letter
                num_substrings += 1
        return num_substrings
    
    def partitionStringSet(self, s: str) -> int:
        so_far = set()
        num_substrings = 1
        for letter in s:
            if letter in so_far:
                so_far = set()
                num_substrings += 1
            so_far.add(letter)
        return num_substrings
    
class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.cases = {
            "abacaba": 4,
            "a": 1,
            "aa": 2,
            "aaa": 3,
        }
    
    def test_string(self):
        for s, expected in self.cases.items():
            self.assertEqual(self.solution.partitionString(s), expected)
    
    def test_set(self):
        for s, expected in self.cases.items():
            self.assertEqual(self.solution.partitionStringSet(s), expected)


if __name__ == "__main__":
    unittest.main()