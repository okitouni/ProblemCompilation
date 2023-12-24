# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.
from unittest import TestCase, main


def count_diff(s, start):
    count = 0
    for char in s:
        if char != start:
            count += 1
        start = "1" if start != "1" else "0"
    return count


class Solution:
    def minOperations(self, s: str) -> int:
        return min(count_diff(s, "0"), count_diff(s, "1"))


def flip(char):
    if char != "1":
        return "1"
    else:
        return "0"


class Solution2:
    def minOperations(self, s: str) -> int:
        keep_path_count = 0
        count = 1
        current = s[0]
        for char in s[1:]:
            if char == current:
                keep_path_count += 1
            else:
                count += 1
            current = flip(current)
        return min(count, keep_path_count)


class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.minOperations("0100"), 1)

    def test_2(self):
        self.assertEqual(self.solution.minOperations("10"), 0)

    def test_3(self):
        self.assertEqual(self.solution.minOperations("1111"), 2)

    def test_4(self):
        self.assertEqual(self.solution.minOperations("10010100"), 3)

    def test_5(self):
        self.assertEqual(self.solution.minOperations("01001001101"), 5)

    def test_6(self):
        self.assertEqual(self.solution.minOperations("0000"), 2)

    def test_7(self):
        self.assertEqual(self.solution.minOperations("1110"), 1)


if __name__ == "__main__":
    main()
