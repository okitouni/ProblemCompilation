# Definition for a binary tree node.
# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"
        

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert_subtree(node: Optional[TreeNode]=root):
        if node is None: return None
        node.left, node.right = node.right, node.left
        invert_subtree(node.left)
        invert_subtree(node.right)
        return node
    return invert_subtree()

# test cases
root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4, TreeNode(5))), TreeNode(2)) # depth 4
print(invertTree(root))
root = TreeNode(0) # depth 1
print(invertTree(root))
root = None # depth 0
print(invertTree(root))
