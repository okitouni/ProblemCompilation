# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        prev_steps, steps = 1, 1
        for _ in range(1, n):
            steps, prev_steps = prev_steps + steps, steps
        return steps
        