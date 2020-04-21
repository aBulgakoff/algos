from typing import List


def dfs(grid, r, c):
    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] != '1':
        return

    grid[r][c] = '0'
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        qty = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    dfs(grid, i, j)
                    qty += 1
        return qty
