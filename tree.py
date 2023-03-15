from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"



def make_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        node = queue.pop(0)
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root