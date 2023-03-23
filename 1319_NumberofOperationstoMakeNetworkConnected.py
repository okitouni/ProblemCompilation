# # 1319. Number of Operations to Make Network Connected

# There are n computers numbered from 0 to n - 1 connected by ethernet 
# cables connections forming a network where connections[i] = [ai, bi] 
# represents a connection between computers ai and bi. Any computer can 
# reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract 
# certain cables between two directly connected computers, and place them 
# between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make
#  all the computers connected. If it is not possible, return -1.
from typing import List
import unittest


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        connected_componenets = list(range(n))
        edges_per_componenet = [0] * n

        def get_parent(node):
            parent = connected_componenets[node]
            if parent != node:
                connected_componenets[node] = get_parent(parent)
            return connected_componenets[node]

        def set_parent(node, parent):
            connected_componenets[node] = get_parent(parent)

        for node1, node2 in connections:
            set_parent(get_parent(node2), get_parent(node1))

        # # clean up some loose ends
        for node in range(n):
            get_parent(node)

        # compute nodes per cc
        # and number of disjoint cc's we need to connect
        # cc_nodes = defaultdict(int)
        cc_nodes = [0] * n
        require_connection = 0
        for cc in connected_componenets:
            if cc_nodes[cc] == 0:
                require_connection += 1
            cc_nodes[cc] += 1
        require_connection -= 1

        # compute edges per cc
        for node1, node2 in connections:
            edges_per_componenet[get_parent(node1)] += 1
        # find redundancies
        redundant_edges = 0
        for cc, nodes in enumerate(cc_nodes):
            if nodes:
                redundant_edges += edges_per_componenet[cc] - nodes + 1
        # return
        if redundant_edges >= require_connection:
            return require_connection
        else:
            return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_makeConnected(self):
        self.assertEqual(self.s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]), 1)
        self.assertEqual(
            self.s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]), 2
        )
        self.assertEqual(self.s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]), -1)
        self.assertEqual(self.s.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]), 0)


if __name__ == "__main__":
    unittest.main()
