# 1422. Maximum Score After Splitting a String
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
from unittest import TestCase, main

class Solution:
    def maxScore(self, s: str) -> int:
        ones, score, max_score = 0, 0, -1
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            else:
                score += 1
            if i != len(s) - 1:
                max_score = max(max_score, score - ones)
        return max_score + ones
    

class TestSolution(TestCase):
    def test1(self):
        self.assertEqual(Solution().maxScore("011101"), 5)

    def test2(self):
        self.assertEqual(Solution().maxScore("00111"), 5)

    def test3(self):
        self.assertEqual(Solution().maxScore("1111"), 3)

    def test4(self):
        self.assertEqual(Solution().maxScore("00"), 1)

    def test5(self):
        self.assertEqual(Solution().maxScore("11"), 1)
        
    
if __name__ == "__main__":
    main()
    