# 455. Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
from unittest import TestCase, main
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greed_idx = 0
        for size in s:
            if greed_idx == len(g): break
            if size >= g[greed_idx]:
                greed_idx += 1
        return greed_idx

class TestSolution(TestCase):
    def setUp(self):
        self.inou = [
            ([1,2,3], [1,1], 1),
            ([1,2], [1,2,3], 2)
        ]
        self.sol = Solution()
        
    def test_findContentChildren(self):
        for p1, p2, correct_ans in self.inou:
            ans = self.sol.findContentChildren(p1, p2)
            self.assertEqual(ans, correct_ans)

if __name__ == "__main__":
    main()