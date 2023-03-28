# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

from typing import List
import unittest

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float("inf")] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                best = min(dp[i+1][j], dp[i][j+1])
                if best == float("inf"):
                    best = 0
                dp[i][j] = grid[i][j] + best
        return dp[0][0]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    def test_minPathSum(self):
        self.assertEqual(self.s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
        self.assertEqual(self.s.minPathSum([[1,2,3],[4,5,6]]), 12)
        self.assertEqual(self.s.minPathSum([[1,2,3]]), 6)
        self.assertEqual(self.s.minPathSum([[1],[2],[3]]), 6)
    

if __name__ == "__main__":
    unittest.main()