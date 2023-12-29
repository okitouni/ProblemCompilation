# 1335. Minimum Difficulty of a Job Schedule
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
from functools import cache
from typing import List
from unittest import TestCase, main

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: return -1
        if d == n: return sum(jobDifficulty)

        @cache
        def dfs(job_id=0, days_left=d):
            if days_left == 1: 
                return max(jobDifficulty[job_id:])
            result = float('inf')

            days_left-=1
            current_stack_max = jobDifficulty[job_id]
            for i in range(job_id, n-days_left):
                current_stack_max = max(current_stack_max, jobDifficulty[i])
                result = min(result, dfs(i+1, days_left) + current_stack_max)
            return result
        return dfs()

class testSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([6,5,4,3,2,1], 2, 7),
            ([9,9,9], 4, -1),
            ([1,1,1], 3, 3),
            ([7,1,7,1,7,1], 3, 15),
            ([11,111,22,222,33,333,44,444], 6, 843)
        ]
    def test_minDifficulty(self):
        for p1, p2, p3 in self.inou:
            with self.subTest(input=p1, expected=p3):
                self.assertEqual(self.solution.minDifficulty(p1, p2), p3)
                
if __name__ == "__main__":
    main()