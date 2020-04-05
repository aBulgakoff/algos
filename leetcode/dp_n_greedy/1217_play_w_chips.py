from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = even = 0
        for pos in chips:
            if pos % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)
