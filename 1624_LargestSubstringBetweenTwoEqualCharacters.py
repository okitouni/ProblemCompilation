# 1624. Largest Substring Between Two Equal Characters

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

from unittest import TestCase, main


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        result = -1
        for idx, char in enumerate(s):
            if char not in seen:
                seen[char] = idx
            else:
                result = max(idx - seen[char] - 1, result)
        return result


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ("aa", 0),
            ("abca", 2),
            ("cbzxy", -1),
            ("cabbac", 4),
        ]

    def test_maxLengthBetweenEqualCharacters(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.maxLengthBetweenEqualCharacters(p1), p2)


if __name__ == "__main__":
    main()
