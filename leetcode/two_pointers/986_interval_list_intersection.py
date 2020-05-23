from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = list()
        ai = bi = 0

        while ai < len(A) and bi < len(B):
            first = max(A[ai][0], B[bi][0])
            last = min(A[ai][1], B[bi][1])
            if first <= last:
                result.append([first, last])

            if A[ai][1] < B[bi][1]:
                ai += 1
            else:
                bi += 1

        return result
