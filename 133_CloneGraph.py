# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
from collections import deque
import unittest

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        new_nodes = [None] * 101
        q = [node]
        while q:
            node = q.pop()
            if new_nodes[node.val]: continue
            new_nodes[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                if new_nodes[neighbor.val]:
                    new_nodes[neighbor.val].neighbors.append(new_nodes[node.val])
                    new_nodes[node.val].neighbors.append(new_nodes[neighbor.val])
                else:
                    q.append(neighbor)
        return new_nodes[1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        new_node1 = Solution().cloneGraph(node1)
        self.assertEqual(new_node1.val, 1)
        self.assertEqual({node.val for node in new_node1.neighbors}, {2, 4})
        self.assertEqual({node.val for node in new_node1.neighbors[0].neighbors}, {1, 3})
        self.assertEqual({node.val for node in new_node1.neighbors[1].neighbors}, {1, 3})
        # still need to test the other nodes

    
if __name__ == "__main__":
    unittest.main()