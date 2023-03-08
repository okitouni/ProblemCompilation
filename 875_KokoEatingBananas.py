# # 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.
from typing import List
import math
import unittest

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(speed):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/speed)
                if total_time > h:
                    return False
            return True

        u = max(piles)
        l = 1
        while l < u:
            mid = (l + u)//2
            if is_valid(mid):
                u = mid
            else:
                l = mid + 1
        return u


class Test(unittest.TestCase):
    def test_minEatingSpeed(self):
        t = Solution()
        self.assertEqual(t.minEatingSpeed([3,6,7,11], 8), 4)
        self.assertEqual(t.minEatingSpeed([30,11,23,4,20], 5), 30)
        self.assertEqual(t.minEatingSpeed([30,11,23,4,20], 6), 23)

if __name__ == "__main__":
    unittest.main()
    