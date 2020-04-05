import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = [-1 * element for element in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            product = largest - next_largest
            if product:
                heapq.heappush(stones, product)
        return -1 * heapq.heappop(stones) if stones else 0
