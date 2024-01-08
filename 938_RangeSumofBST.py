# 938. Range Sum of BST

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def dfs(node):
            nonlocal total
            if node is not None:
                if node.val >= low and node.val <= high:
                    total += node.val
                dfs(node.left), dfs(node.right)

        dfs(root)
        return total

