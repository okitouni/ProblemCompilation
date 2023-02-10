# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.


def farthest_water(grid):
    n = len(grid)
    dp = [[2 * n] * n for _ in range(n)]

    def neighbor_distances(row, col, lowerleft=True):
        d = dp[row][col]
        if lowerleft:
            if row > 0 and d > dp[row - 1][col]:
                d = dp[row - 1][col] + 1
            if col > 0 and d > dp[row][col - 1]:
                d = dp[row][col - 1] + 1
        else:
            if row < n - 1 and d > dp[row + 1][col]:
                d = dp[row + 1][col] + 1
            if col < n - 1 and d > dp[row][col + 1]:
                d = dp[row][col + 1] + 1
        return d

    # first pass from topleft to bottom right
    for row in range(n):
        for col in range(n):
            if grid[row][col]:
                dp[row][col] = 0
            else:
                dp[row][col] = neighbor_distances(row, col)
    # second pass from bottom right to top left
    MAX = 0
    for row in range(n - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if grid[row][col]:
                dp[row][col] = 0
            else:
                dp[row][col] = neighbor_distances(row, col, lowerleft=False)
                if dp[row][col] > MAX:
                    MAX = dp[row][col]
    if MAX == 0 or MAX == 2 * n:
        return -1
    return MAX


print(farthest_water([[0, 1], [1, 1]]))
