# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.


from collections import defaultdict, deque
from typing import List
import unittest


def minJumps(arr: List[int]) -> int:
    graph = defaultdict(list)
    for idx, num in enumerate(arr):
        graph[num].append(idx)

    def get_children(node: idx, neighbors=False):
        if neighbors:
            children = []
            if node > 0:
                children.append(node - 1)
            if node < len(arr) - 1:
                children.append(node + 1)
            return children
        else:
            return graph[arr[node]][::-1]

    q = deque([0])
    visited = set()
    k = 0
    while q:
        tmp = deque()
        while q:
            node = q.popleft()
            if node == len(arr) - 1:
                return k
            if node not in visited:
                for child in get_children(node):
                    if child not in visited and child != node:
                        tmp.append(child)
                        visited.add(child)  # mark everything as visited
                        # because all nodes with this value are connected
                        # only missing direct neighbors
                visited.add(node)
            # check 2 neighbors we may have skipped
            # when we added child to visited
            for child in get_children(node, True):
                if child not in visited:
                    tmp.append(child)
        q = tmp
        k += 1
    return k


class Test(unittest.TestCase):
    def test_minJumps(self):
        arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
        self.assertEqual(minJumps(arr), 3)
        arr = [7]
        self.assertEqual(minJumps(arr), 0)
        arr = [7, 6, 9, 6, 9, 6, 9, 7]
        self.assertEqual(minJumps(arr), 1)
        arr = [6, 1, 9]
        self.assertEqual(minJumps(arr), 2)
        arr = [11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]
        self.assertEqual(minJumps(arr), 3)


if __name__ == "__main__":
    unittest.main()
