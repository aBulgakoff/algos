from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(tuple(obst) for obst in obstacles)
        x, y = 0, 0
        dir_x, dir_y = 0, 1
        max_dist = 0
        for comm in commands:
            if comm == -2:
                dir_x, dir_y = -dir_y, dir_x
            elif comm == -1:
                dir_x, dir_y = dir_y, -dir_x
            else:
                while comm and (nxt_x := x + dir_x, nxt_y := y + dir_y) not in obstacles:
                    x, y = nxt_x, nxt_y
                    comm -= 1
                max_dist = max(max_dist, x * x + y * y)
        return max_dist
