# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
from collections import deque
from typing import Optional
from tree import TreeNode, make_tree
import unittest


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        saw_none = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    saw_none = True
                    continue
                q.append(node.left)
                q.append(node.right)
                if saw_none:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.examples = [
            ([1, 2, 3, 4, 5, 6], True),
            ([1, 2, 3, 4, 5, None, 7], False),
            ([1], True),
            ([1, 3, 4, None, 5], False),
        ]

    def test_isCompleteTree(self):
        for nodes, expected in self.examples:
            print("testing nodes: ", nodes, "expected: ", expected)
            self.assertEqual(self.sol.isCompleteTree(make_tree(nodes)), expected)


if __name__ == "__main__":
    unittest.main()
