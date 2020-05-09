from typing import List


class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        fst_pair, snd_pair = coord[0], coord[1]
        x_diff, y_diff = (snd - fst for fst, snd in zip(fst_pair, snd_pair))
        return all(x_diff * (y - snd_pair[1]) == (x - snd_pair[0]) * y_diff for x, y in coord)
