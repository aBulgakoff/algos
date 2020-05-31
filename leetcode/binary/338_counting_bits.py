from itertools import repeat
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        count = list(repeat(0, num + 1))
        for i in range(1, num + 1):
            count[i] = count[i >> 1] + i % 2
        return count
