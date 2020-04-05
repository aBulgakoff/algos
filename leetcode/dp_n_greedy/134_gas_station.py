from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ix_start = total_balance = next_balance = 0
        for ix, (gas_curr_st, cost_next_trip) in enumerate(zip(gas, cost)):
            next_trip = gas_curr_st - cost_next_trip

            total_balance += next_trip
            next_balance += next_trip

            if next_balance < 0:
                ix_start = ix + 1
                next_balance = 0

        return ix_start if total_balance >= 0 else -1
