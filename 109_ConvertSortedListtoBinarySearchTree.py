# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
# height-balanced
#  binary search tree.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        lst = []
        size = 0
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
            size += 1

        def fill_tree(l=0, h=size - 1):
            if l > h:
                return None
            mid = (l + h) // 2
            node = TreeNode(lst[mid])
            node.right = fill_tree(mid + 1, h)
            node.left = fill_tree(l, mid - 1)
            return node

        return fill_tree()
