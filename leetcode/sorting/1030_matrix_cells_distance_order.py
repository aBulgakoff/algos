from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = [[r, c] for r in range(R) for c in range(C)]
        matrix.sort(key=lambda point: abs(point[0] - r0) + abs(point[1] - c0))
        return matrix
