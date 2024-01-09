# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.


# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            leaves = []

            def dfs(node):
                if node is not None:
                    left, right = dfs(node.left), dfs(node.right)
                    if left and right:
                        leaves.append(node.val)
                    return False
                return True

            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)
