from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for index in range(len(A) - 2):
            if A[index] < A[index + 1] + A[index + 2]:
                return A[index] + A[index + 1] + A[index + 2]
        return 0
