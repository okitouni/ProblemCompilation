# # You have n dice, and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
from unittest import TestCase, main

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(1, min(target, k) + 1):
            dp[0][i] = 1
        for row in range(1, n):
            for cur_sum in range(row, min(target, (row+1) * k) + 1):
                for dice_roll in range(1, k+1):
                    if dice_roll > cur_sum:
                        break
                    dp[row][cur_sum] += dp[row-1][cur_sum-dice_roll]
                dp[row][cur_sum] %= mod
        return dp[-1][-1]
    
class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inputs = [
            (1, 6, 3, 1),
            (2, 6, 7, 6),
            (2, 5, 10, 1),
            (1, 2, 3, 0),
            (30, 30, 500, 222616187)
        ]
        
    def test_numRollsToTarget(self):
        for p1, p2, p3, p4 in self.inputs:
            with self.subTest(input=(p1, p2, p3), expected=p4):
                self.assertEqual(self.solution.numRollsToTarget(p1, p2, p3), p4)
                
if __name__ == "__main__":
    main()
