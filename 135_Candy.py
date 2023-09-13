"""
135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""
from typing import List
from unittest import TestCase, main

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # candies[i] for 1,..., i
        # candies[i+1] = 1 if ratings[i+1] <= ratings[i] else ratings[i] + 1
        res = 1      # final result
        prev = 1     # previous kid's number of candies
        last_leq = 0 # last time kid had less than or equal to rating
        last_leq_value = 1
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]: # new kid is higher rated
                prev += 1 # gets one more candy than prev
                last_leq = i 
                last_leq_value = prev
            elif ratings[i-1] == ratings[i]:
                prev = 1 # if equal I can lower to the minimum
                last_leq = i
                last_leq_value = prev
            else:
                if prev == 1:
                    res += i - last_leq # update all previous kids until we hit a kid with an lower or equal rating
                    if last_leq_value > (i - last_leq):
                        res -= 1
                    else:
                        last_leq_value += 1
                prev = 1 # new kid has less rating
                
            res += prev
        return res
    
class Test(TestCase):
    def setUp(self) -> None:
        self.ratings = [1,0,2]
        self.sol = Solution()

    def test_candy(self) -> None:
        self.assertEqual(
            self.sol.candy(self.ratings),
            5
        )
        
if __name__ == "__main__":
    main()