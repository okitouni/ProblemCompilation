# 1026. Maximum Difference Between Node and Ancestor
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node=root, ancestor_min=float('inf'), ancestor_max=float('-inf')):
            if node is None:
                return ancestor_max - ancestor_min
            ancestor_max = max(ancestor_max, node.val)
            ancestor_min = min(ancestor_min, node.val)
            return max(
                helper(node.left, ancestor_min, ancestor_max), 
                helper(node.right, ancestor_min, ancestor_max)
                )
        return helper()