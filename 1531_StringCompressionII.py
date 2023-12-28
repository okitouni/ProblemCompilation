# 1531. String Compression II

# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

# Notice that in this problem, we are not adding '1' after single characters.

# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

# Find the minimum length of the run-length encoded version of s after deleting at most k characters.
from functools import lru_cache
from unittest import TestCase, main

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(i, prev_char, prev_char_count, deletions):
            if deletions < 0:
                return float('inf')
            if i == len(s):
                return 0
            if s[i] == prev_char:
                # if the current character is the same as the previous character, 
                # the count of the previous character will increase by 1
                # the number of characters changed will be 1 if the previous count is 1, 9, or 99, otherwise 0
                diff = 1 if prev_char_count == 1 or prev_char_count == 9 or prev_char_count == 99 else 0
                keep_case = dfs(i + 1, prev_char, prev_char_count + 1, deletions) + diff
                delete_case = dfs(i + 1, prev_char, prev_char_count, deletions - 1)
            else:
                keep_case = 1 + dfs(i + 1, s[i], 1, deletions)
                delete_case = dfs(i + 1, prev_char, prev_char_count, deletions - 1)
            return min(keep_case, delete_case)
        return dfs(i=0, prev_char='', prev_char_count=0, deletions=k)
    
    
    
    
class TestSolution(TestCase):
    def test1(self):
        self.assertEqual(Solution().getLengthOfOptimalCompression("aaabcccd", 2), 4)
        
    def test2(self):
        self.assertEqual(Solution().getLengthOfOptimalCompression("aabbaa", 2), 2)
        
        
if __name__ == "__main__":
    main()