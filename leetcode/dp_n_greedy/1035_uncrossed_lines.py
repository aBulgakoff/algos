from itertools import repeat
from typing import List


class Solution:  # DP O(N*m) / O(N*M)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A) + 1, len(B) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class Solution2:  # DP O(N*M) / O(N)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A) + 1, len(B) + 1
        dp = [0 for _ in range(n)]

        for i in range(1, m):

            row = [0 for _ in range(n)]
            for j in range(1, n):

                if A[i - 1] == B[j - 1]:
                    row[j] = 1 + dp[j - 1]
                else:
                    row[j] = max(dp[j], row[j - 1])
            dp = row
        return dp[-1]


class Solution3:    # DP O(N*M) / O(N)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A) + 1, len(B) + 1
        dp = [*repeat(0, n)]

        for i in range(1, m):
            row = [*repeat(0, n)]
            for j in range(1, n):
                row[j] = (1 + dp[j - 1]
                          if A[i - 1] == B[j - 1]
                          else max(row[j - 1], dp[j])
                          )
            dp = row
        return dp[-1]
