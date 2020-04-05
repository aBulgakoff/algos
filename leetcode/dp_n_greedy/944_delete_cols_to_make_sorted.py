from typing import List


class Solution:  # greedy
    def minDeletionSize(self, A: List[str]) -> int:
        return len([i for i, s in enumerate(zip(*A)) if not all(t <= n for t, n in zip(s, s[1:]))])


class Solution2:  # greedy
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(c > n for c, n in zip(st, st[1:])) for st in zip(*A))
