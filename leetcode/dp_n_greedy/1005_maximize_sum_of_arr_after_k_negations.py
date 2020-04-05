import heapq
from typing import List


class Solution:  # greedy
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        ix = qty_negative = has_zero = 0
        for num in A:
            if num < 0:
                qty_negative += 1
            elif num == 0:
                has_zero = True

        if qty_negative > K:
            A.sort()

        while ix < len(A) and K:
            if A[ix] < 0:
                A[ix] = -A[ix]
                K -= 1
            ix += 1

        if K % 2 and not has_zero:
            ix_min, min_elem = 0, float('+inf')
            for ix, elem in enumerate(A):
                if elem < min_elem:
                    ix_min, min_elem = ix, elem
            A[ix_min] = -min_elem
        return sum(A)


class Solution2:  # greedy # heap
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, -heapq.heappop(A))
        return sum(A)
