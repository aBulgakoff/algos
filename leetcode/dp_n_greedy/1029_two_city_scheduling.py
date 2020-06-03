from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ix_a, ix_b, min_costs = 0, len(costs) - 1, 0
        costs.sort(key=lambda x: x[0] - x[1])
        while ix_a < ix_b:
            min_costs += costs[ix_a][0] + costs[ix_b][1]
            ix_a += 1
            ix_b -= 1
        return min_costs


# Sort by a gain which company has
# by sending a person to city A and not to city B

class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        return sum(a for a, _ in costs[:n]) + sum(b for _, b in costs[n:])
