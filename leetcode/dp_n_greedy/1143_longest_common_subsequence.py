from functools import lru_cache


class Solution:  # recursion + memorization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def LCS(i: int, j: int) -> int:
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + LCS(i + 1, j + 1)
            else:
                return max(LCS(i + 1, j), LCS(i, j + 1))

        return LCS(0, 0)


class Solution2:  # dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    grid[row][col] = 1 + grid[row + 1][col + 1]
                else:
                    grid[row][col] = max(grid[row + 1][col], grid[row][col + 1])
        return grid[0][0]


class Solution3:  # dp space O(min(t1, t2))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        prev = [0 for _ in range(len(text1) + 1)]
        for col in reversed(range(len(text2))):
            cur = [0 for _ in range(len(text1) + 1)]
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    cur[row] = 1 + prev[row + 1]
                else:
                    cur[row] = max(prev[row], cur[row + 1])
            prev = cur
        return prev[0]
