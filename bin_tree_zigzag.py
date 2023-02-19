# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
from tree import TreeNode
from collections import deque, defaultdict

def zigzag(root):
    q = deque([(root, 0)])
    levels = defaultdict(list)
    while q:
        node, depth = q.popleft()
        if node:
            for child in [node.left, node.right]:
                q.append((child, depth+1))
            levels[depth].append(node.val)
    return [lst[::-1] if key % 2 else lst for key, lst in levels.items()]

# test cases
root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4, TreeNode(5))), TreeNode(2)) # depth 4
print(zigzag(root))
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5))) # depth 1
print(zigzag(root))
root = None # depth 0
print(zigzag(root))
