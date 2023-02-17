# 783. Minimum Distance Between BST Nodes
# Given the root of a Binary Search Tree (BST),
# return the minimum difference between the values of any two different nodes in the tree.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_min_dist(root: Optional[TreeNode]) -> int:
    order = [-float("inf")]
    res = float("inf")

    def traversal_order(node: Optional[TreeNode] = root):
        if node is None:
            return
        traversal_order(node.left)
        prev = order.pop()
        nonlocal res
        res = min(node.val - prev, res)
        order.append(node.val)
        traversal_order(node.right)

    traversal_order()
    return res


def get_min_dist2(root: Optional[TreeNode]) -> int:
    def traversal_order(
        node: Optional[TreeNode] = root, lower=-float("inf"), upper=float("inf")
    ):
        if node is None:
            return upper - lower
        return min(
            traversal_order(node.left, lower, node.val),
            traversal_order(node.right, node.val, upper),
        )
    return traversal_order()


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(get_min_dist2(root))
