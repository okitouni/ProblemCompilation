# 1235. Maximum Profit in Job Scheduling

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.
from unittest import TestCase, main

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda element: element[1])
        
        dp = [(0, 0)]
        for start, end, p in jobs:
            p = self.find_last_nonconflict(dp, start) + p
            if p > dp[-1][1]:
                dp.append((end, p))
        return dp[-1][1]
                 
    def find_last_nonconflict(self, dp, start):
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid][0] <= start:
                low = mid + 1
            else:
                high = mid - 1
        return dp[high][1]
    
    
class TestSolution(TestCase):
    def setUp(self):
        self.cases = [
            ([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
            ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
            ([1,1,1], [2,3,4], [5,6,4], 6)
        ]
    
    def test(self):
        s = Solution()
        for startTime, endTime, profit, expected in self.cases:
            self.assertEqual(s.jobScheduling(startTime, endTime, profit), expected)
            
if __name__ == "__main__":
    main()
    