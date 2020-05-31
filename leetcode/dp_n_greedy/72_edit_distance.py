from itertools import repeat


class Solution: # dp # Levenshtein distance
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) + 1, len(word2) + 1
        dp = [list(repeat(0, n)) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not i:
                    dp[i][j] = j

                elif not j:
                    dp[i][j] = i

                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                       dp[i - 1][j],
                                       dp[i][j - 1]
                                       )
        return dp[-1][-1]
