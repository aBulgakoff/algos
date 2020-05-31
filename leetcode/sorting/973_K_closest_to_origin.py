from typing import List


def pwtwo(x: int) -> int:
    return pow(x, 2)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: sum(map(pwtwo, x)))
        return points[:K]
