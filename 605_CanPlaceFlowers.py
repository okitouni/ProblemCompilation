# # 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
from typing import List
import unittest

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev_full = False
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                prev_full = True
                continue
            if prev_full:
                prev_full = False
                continue
            if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                prev_full = True
                n-=1
        return n <= 0
           
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().canPlaceFlowers([1,0,0,0,1], 1), True)
    def test2(self):
        self.assertEqual(Solution().canPlaceFlowers([1,0,0,0,1], 2), False)
    def test3(self):
        self.assertEqual(Solution().canPlaceFlowers([1,0,1,0,1, 0, 0], 1), True)
    def test4(self):
        self.assertEqual(Solution().canPlaceFlowers([1,0,0,0,1, 0, 0], 2), True)
    

if __name__ == '__main__':
    unittest.main()