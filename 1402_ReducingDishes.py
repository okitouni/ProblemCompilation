# 1402. Reducing Dishes
# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
from typing import List
import unittest

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        current_total = 0
        ans = 0
        for s in satisfaction:
            current_total += s 
            if current_total < 0:  break # next contribution must be positive
            ans += current_total # repeats previous contributions once
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_maxSatisfaction(self):
        self.assertEqual(self.solution.maxSatisfaction([-1,-8,0,5,-9]), 14)
        self.assertEqual(self.solution.maxSatisfaction([4,3,2]), 20)
        self.assertEqual(self.solution.maxSatisfaction([-1,-4,-5]), 0)
        self.assertEqual(self.solution.maxSatisfaction([-2,5,-1,0,3,-3]), 35)
    
if __name__ == '__main__':
    unittest.main()