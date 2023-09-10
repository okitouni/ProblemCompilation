"""1359. Count All Valid Pickup and Delivery Options
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.
"""
from unittest import TestCase

MOD = int(1e9+7)
class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(2, n+1):
            res = (res * (2*i - 1) * i) % MOD
        return res 
    
    
class TestSolution(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()
        self.testcases = [
            (1, 1),
            (2, 6),
            (3, 90),
        ]
        
    def test_countOrders(self):
        for n, expected in self.testcases:
            self.assertEqual(self.solution.countOrders(n), expected)
    
if __name__ == '__main__':
    test = TestSolution()
    test.test_countOrders()
    print('All Passed!')