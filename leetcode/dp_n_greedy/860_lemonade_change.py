from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        price, cash = 5, {5: 0, 10: 0, 20: 0}
        for bill in bills:
            cash[bill] += 1
            change = bill - price
            while change:
                if change >= 10 and cash[10] > 0:
                    cash[10] -= 1
                    change -= 10
                elif change >= 5 and cash[5] > 0:
                    cash[5] -= 1
                    change -= 5
                else:
                    return False
        return True
