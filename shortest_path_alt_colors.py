# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
import collections


def shortest_paths(n, redEdges, blueEdges):
    distances = [-1] * n
    distances[0] = 0

    def get_graph(edges):
        children = collections.defaultdict(list)
        for v1, v2 in edges:
            children[v1].append(v2)
        return children

    children = [get_graph(redEdges), get_graph(blueEdges)]

    visited = set()
    q = collections.deque([(0, 0, 0), (0, 0, 1)])
    while q:
        node, dist, color = q.popleft()
        visited.add((node, color))
        if distances[node] < 0:
            distances[node] = dist
        dist += 1
        color = (color + 1) % 2
        for child in children[color][node]:
            if (child,color) not in visited:
                q.append((child, dist, color))

    return distances


redEdges = [[0, 0], [0, 3], [3, 2], [1, 1]]
blueEdges = [
    [0, 1],
    [1, 2],
    [3, 1],
]
print('redEdges', redEdges)
print('blueEdges', blueEdges)
print(shortest_paths(4, redEdges, blueEdges))
