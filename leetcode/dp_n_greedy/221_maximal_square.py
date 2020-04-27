from typing import List


class Solution:
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
            max_sq = max(max_sq, dp[row])
        msq = max(max(row) for row in dp)
        return msq * msq
