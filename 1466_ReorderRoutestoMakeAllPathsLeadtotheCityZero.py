# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

from collections import deque
from typing import List
import unittest


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in  range(n)]
        for src, tgt in connections:
            graph[src].append(tgt)
            graph[tgt].append(src)
        connections = {tuple(pair) for pair in connections}

        q = deque([0])
        bad_routes = 0
        visited = [0] * n
        while q:
            node = q.popleft()
            visited[node] = 1
            for child in graph[node]:
                if not visited[child]:
                    q.append(child)
                    if (child, node) not in connections:
                        bad_routes += 1
        return bad_routes
       

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        self.assertEqual(self.solution.minReorder(n, connections), 3)

    def test_2(self):
        n = 5
        connections = [[1,0],[1,2],[3,2],[3,4]]
        self.assertEqual(self.solution.minReorder(n, connections), 2)

    def test_3(self):
        n = 3
        connections = [[1,0],[2,0]]
        self.assertEqual(self.solution.minReorder(n, connections), 0)

    
if __name__ == '__main__':
    unittest.main()