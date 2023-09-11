"""1282. Group the People Given the Group Size They Belong To
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""
from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        res = []
        for person_id, group_size in enumerate(groupSizes):
            groups[group_size].append(person_id)
            if len(groups[group_size]) == group_size:
                res.append(groups[group_size])
                groups[group_size] = []
        return res
    
class TestSolution(TestCase):
    def __init__(self) -> None:
        super().__init__()
        self.solution = Solution()
        # TODO come up with way to make test cases order agnostic
        self.test_cases = [
            ([3, 3, 3, 3, 3, 1, 3], [[0, 1, 2], [5], [3, 4, 6]]),
            ([2, 1, 3, 3, 3, 2], [[1], [2, 3, 4], [0, 5]]),
        ]

    def test_solution(self):
        for test_case, expected_result in self.test_cases:
            self.assertEqual(
                self.solution.groupThePeople(test_case), expected_result
            )
        
if __name__ == "__main__":
    test = TestSolution()
    test.test_solution()
    print("All Tests passed")