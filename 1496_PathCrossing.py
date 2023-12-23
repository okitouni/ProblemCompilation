# 1496. Path Crossing
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
from unittest import TestCase, main

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False

class Test(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_isPathCrossing_1(self):
        path = "NES"
        self.assertFalse(self.sol.isPathCrossing(path))

    def test_isPathCrossing_2(self):
        path = "NESWW"
        self.assertTrue(self.sol.isPathCrossing(path))

    def test_isPathCrossing_3(self):
        path = "NNSWWEWSSESSWENNW"
        self.assertTrue(self.sol.isPathCrossing(path))
        
if __name__ == "__main__":
    main()
