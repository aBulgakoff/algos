from collections import deque
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = deque(s)
        for direction, amount in shift:
            s.rotate(amount if direction else -amount)
        return ''.join(s)


class Solution2:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = deque(s)
        s.rotate(sum(map(lambda x: x[1] if x[0] else -x[1], shift)) % len(s))
        return ''.join(s)


class Solution3:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        rotation = sum(map(lambda x: -x[1] if x[0] else x[1], shift)) % len(s)
        return s[rotation:] + s[:rotation]
