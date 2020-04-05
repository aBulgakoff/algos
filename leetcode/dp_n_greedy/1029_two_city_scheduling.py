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
