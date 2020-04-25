from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        qty = current = 0
        accumul = Counter((0,))

        for num in nums:
            current += num
            qty += accumul[current - k]
            accumul[current] += 1
        return qty
