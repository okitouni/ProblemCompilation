"""1647. Minimum Deletions to Make Character Frequencies Unique

"""

from collections import Counter
from unittest import TestCase

class Solution:
    def minDeletions(self, s: str) -> int:
        char_freq = Counter(s)
        freqs = set()
        deletions = 0

        for freq in char_freq.values():
            while freq in freqs and freq:
                freq -= 1
                deletions += 1
            freqs.add(freq)
        return deletions
    
class TestSolution(TestCase):
    def __init__(self):
        super().__init__()
        self.solution = Solution()
        self.test_cases = [("a", 0), ("aaabbbcc", 2), ("ceabaacb", 2) ]
            
    def test_minDeletions(self):
        for case in self.test_cases:
            self.assertEqual(self.solution.minDeletions(case[0]), case[1])

if __name__ == "__main__":            
    test = TestSolution()
    test.test_minDeletions()
    print("All Tests passed")
