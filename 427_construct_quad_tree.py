# Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

# Return the root of the Quad-Tree representing the grid.

# Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

# A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

# val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
# isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# }
# We can construct a Quad-Tree from a two-dimensional area using the following steps:

# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
# If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
# Recurse for each of the children with the proper sub-grid.
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    
    def __repr__(self):
        return f'Node({self.val}, {self.isLeaf}, {self.topLeft}, {self.topRight}, {self.bottomLeft}, {self.bottomRight})'

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(grid):
            if len(grid) == 1:
                return Node(grid[0][0], True, None, None, None, None)
            n = len(grid)
            topLeft = dfs([row[:n//2] for row in grid[:n//2]])
            topRight = dfs([row[n//2:] for row in grid[:n//2]])
            bottomLeft = dfs([row[:n//2] for row in grid[n//2:]])
            bottomRight = dfs([row[n//2:] for row in grid[n//2:]])
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(grid)

if __name__ == '__main__':
    solution = Solution()
    grid = [[0,1],[1,0]]
    print(solution.construct(grid))
