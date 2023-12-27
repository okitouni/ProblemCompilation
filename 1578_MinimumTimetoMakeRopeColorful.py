# 1578. Minimum Time to Make Rope Colorful
# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.
from unittest import TestCase, main


class Solution:
    def minTimeToMakeColorful(self, colors: str, neededTime: list[int]) -> int:
        cost, prev_max = 0, neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                cost += min(prev_max, neededTime[i])
                prev_max = max(prev_max, neededTime[i])
            else:
                prev_max = neededTime[i]
        return cost


class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ("a", [1], 0),
            ("aaabbbc", [1, 2, 3, 4, 5, 6, 7], 12),
        ]

    def test_minTimeToMakeColorful(self):
        for color_list, costs, ans in self.inou:
            self.assertEqual(
                self.solution.minTimeToMakeColorful(color_list, costs), ans
            )

if __name__ == "__main__":
    main()