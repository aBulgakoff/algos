from typing import List


class Solution:  # greedy
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for ix in range(1, len(prices)):
            if prices[ix] > prices[ix - 1]:
                profit += prices[ix] - prices[ix - 1]
        return profit
