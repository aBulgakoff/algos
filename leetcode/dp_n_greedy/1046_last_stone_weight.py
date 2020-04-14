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


class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones[:] = (-1 * stone for stone in stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(
                stones,
                heapq.heappop(stones) - heapq.heappop(stones))
        return -1 * heapq.heappop(stones)
