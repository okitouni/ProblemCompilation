# 1857. Largest Color Value in a Directed Graph
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
from typing import List
from collections import deque, defaultdict
import unittest

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        path_lengths = [defaultdict(int) for _ in range(n)]
        neighbors = [[] for _ in range(n)]
        indegree = [0] * n
        for src, dst in edges:
            neighbors[src].append(dst)
            indegree[dst] += 1
        q = deque(node for node in range(n) if not indegree[node])
        visited = 0  # if num nodes visited is < n then there's a cycle
        result = 0
        while q:
            node = q.popleft()
            node_color = colors[node]
            path_lengths[node][node_color] += 1
            result = max(result, path_lengths[node][node_color])
            visited += 1
            for neighbor in neighbors[node]:
                for color in path_lengths[node]:
                    path_lengths[neighbor][color] = max(path_lengths[neighbor][color], path_lengths[node][color])
                indegree[neighbor] -= 1
                if not indegree[neighbor]: q.append(neighbor)
        if visited < n: return -1
        return result


class TestSolution(unittest.TestCase):
    def test1(self):
        colors = "abaca"
        edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
        self.assertEqual(Solution().largestPathValue(colors, edges), 3)

    def test2(self):
        colors = "a"
        edges = []
        self.assertEqual(Solution().largestPathValue(colors, edges), 1)

    def test3(self):
        colors = "h"
        edges = [[0, 0]]
        self.assertEqual(Solution().largestPathValue(colors, edges), -1)

if __name__ == "__main__":
    unittest.main()