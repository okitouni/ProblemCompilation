# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char not in {"}", "]", ")"}:
                stack.append(char)
            elif not stack:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        return not stack


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().isValid("()"), True)

    def test_2(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)

    def test_3(self):
        self.assertEqual(Solution().isValid("(]"), False)

    def test_4(self):
        self.assertEqual(Solution().isValid("([)]"), False)

    def test_5(self):
        self.assertEqual(Solution().isValid("{[]}"), True)


if __name__ == "__main__":
    unittest.main()
