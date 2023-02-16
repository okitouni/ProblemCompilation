# Maximum Depth of Binary Tree
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    max_depth = 0
    def dfs(node:Optional[TreeNode]=root, depth:Optional[int]=0)->None:
        if node is None: return
        depth+=1
        nonlocal max_depth
        if depth > max_depth: max_depth = depth
        dfs(node.left, depth)
        dfs(node.right, depth)
    dfs()
    return max_depth

# test cases
root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4, TreeNode(5))), TreeNode(2)) # depth 4
print(maxDepth(root))
root = TreeNode(0) # depth 1
print(maxDepth(root))
root = None # depth 0
print(maxDepth(root))
            