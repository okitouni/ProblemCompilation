# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.
from unittest import TestCase, main

class Solution:
    def numDecodings(self, s: str) -> int:
        ways, combined_ways = int(s[0] != '0'), 0
        if '00' in s: return 0
        for i in range(1, len(s)):
            new_ways = 0
            if s[i] != '0':
                new_ways += ways
            if int(s[i-1: i+1]) < 27 and s[i-1] != '0':
                combined_ways = ways - combined_ways
                new_ways += combined_ways
            else:
                combined_ways = 0
            ways = new_ways
        return ways
    
class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inputs = [
            ("12", 2),
            ("226", 3),
            ("0", 0),
            ("06", 0),
            ("111", 3),
            ("10", 1),
            ("100", 0)
        ]
        
    def test_numDecodings(self):
        for p1, p2 in self.inputs:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.numDecodings(p1), p2)

if __name__ == "__main__":
    main()
                
