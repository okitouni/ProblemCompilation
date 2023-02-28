# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

from tree import TreeNode       
from collections import defaultdict
def return_dup_subtree(root : TreeNode):
    subtrees = defaultdict(int)
    subtree_id = dict() 
    res = []
    def dfs(node=root):
        if node is None: return 0
        subtree = (node.val, dfs(node.left), dfs(node.right)) 
        if subtree not in subtree_id:
            subtree_id[subtree] = len(subtree_id) + 1
        curr_id = subtree_id[subtree]
        if subtrees[curr_id] == 1:
            res.append(node)
        subtrees[curr_id] += 1
        return curr_id
    dfs()
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    print(return_dup_subtree(root))