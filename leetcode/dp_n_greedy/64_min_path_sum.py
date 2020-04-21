from itertools import accumulate
from typing import List


class Solution:  # O(rows * cols) space complexity
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # init
        path = [[0 for _ in range(cols)] for _ in range(rows)]
        path[0][0] = grid[0][0]
        # fill in 0-row with previous values of this row
        # since there's no row before
        for col in range(1, cols):
            path[0][col] = grid[0][col] + path[0][col - 1]
        # fill in 0-col with previous values of this col
        # since there's no col before
        for row in range(1, rows):
            path[row][0] = grid[row][0] + path[row - 1][0]

        for row in range(1, rows):
            for col in range(1, cols):
                path[row][col] = min(path[row - 1][col], path[row][col - 1]) + grid[row][col]
        return path[-1][-1]


class Solution2:  # O(cols) space complexity
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        path = [float('inf') for _ in range(cols)]
        for row in range(rows):
            # for row 0 there aren't previous row
            path[0] = grid[row][0] + (path[0] if row != 0 else 0)
            for col in range(1, cols):
                path[col] = min(path[col - 1], path[col]) + grid[row][col]
        return path[-1]


class Solution3:  # O(1) space complexity, in-place
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            if row != 0:
                grid[row][0] += grid[row - 1][0]
            for col in range(1, cols):
                if row != 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
                else:
                    grid[row][col] += grid[row][col - 1]
        return grid[-1][-1]


class Solution4:   # O(1) space complexity, in-place, 0-row pre-process
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        grid[0][:] = accumulate(grid[0])
        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]
            for col in range(1, cols):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]
