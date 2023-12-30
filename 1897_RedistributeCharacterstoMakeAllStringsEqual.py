# 1897. Redistribute Characters to Make All Strings Equal

# You are given an array of strings words (0-indexed).

# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

# Return true if you can make every string in words equal using any number of operations, and false otherwise.
from collections import Counter
from unittest import TestCase, main
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter(words[0])
        for word in words[1:]:
            counter.update(word)
        for count in counter.values():
            if count % len(words) != 0:
                return False
        return True
    
class Test(TestCase):
    def setUP(self):
        self.tests = [
            {
                "input": ["abc","aabc","bc"],
                "output": True
            },
            {
                "input": ["ab","a"],
                "output": False
            }
        ]
    def test_makeEqual(self):
        s = Solution()
        self.setUP()
        for t in self.tests:
            self.assertEqual(
                t["output"],
                s.makeEqual(t["input"])
            )
            
if __name__ == "__main__":
    main()
            
    