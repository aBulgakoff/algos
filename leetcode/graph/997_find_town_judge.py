from itertools import repeat
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N - 1 > len(trust):
            return -1

        to = [*repeat(0, N + 1)]
        fr0m = [*repeat(0, N + 1)]

        for t, f in trust:
            to[t] += 1
            fr0m[f] += 1

        for citizen in range(1, N + 1):
            if not to[citizen] and fr0m[citizen] == N - 1:
                return citizen
        return -1


class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1

        trust_bal = [*repeat(0, N + 1)]

        for t, f in trust:
            trust_bal[t] -= 1
            trust_bal[f] += 1

        for i, score in enumerate(trust_bal[1:], 1):
            if score == N - 1:
                return i
        return -1
