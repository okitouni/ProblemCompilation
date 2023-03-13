# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional
from tree import TreeNode
import unittest

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def similar(left_subtree, right_subtree):
            if not left_subtree or not right_subtree:
                return left_subtree == right_subtree
            if left_subtree.val != right_subtree.val:
                return False
            return similar(left_subtree.left, right_subtree.right) and\
            similar(left_subtree.right, right_subtree.left)
        return similar(root.left, root.right)
    
class TestSolution(unittest.TestCase):
    def make_tree(self, nodes):
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
        
    def setUp(self):
        self.test_cases = [([1,2,2,3,4,4,3], True)]
        self.s = Solution()
    
    def test_isSymmetric(self):
        for i, e in self.test_cases:
            root = self.make_tree(i)
            print("testing", root)
            self.assertEqual(self.s.isSymmetric(root), e)

if __name__ == '__main__':
    unittest.main(verbosity=2)