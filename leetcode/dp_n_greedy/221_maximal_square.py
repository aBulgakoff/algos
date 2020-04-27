from typing import List


class Solution:  # O(row * col) space complexity
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_sq = 0
        if not matrix:
            return max_sq
        dp = [[int(cell) for cell in row] for row in matrix]

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if int(matrix[row][col]):
                    dp[row][col] = 1 + min(dp[row - 1][col],
                                           dp[row][col - 1],
                                           dp[row - 1][col - 1])
                else:
                    dp[row][col] = 0
        return max(max(row) for row in dp) ** 2


class Solution2:  # O(row) space complexity
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ar = 0
        if not matrix:
            return ar

        prev_row = [0 for _ in range(len(matrix[0]))]
        for row in map(lambda row: [*map(int, row)], matrix):
            for j, col in enumerate(row[1:], 1):
                row[j] *= 1 + min(row[j - 1],
                                  prev_row[j],
                                  prev_row[j - 1])
            ar = max(ar, max(row) ** 2)
            prev_row = row
        return ar
