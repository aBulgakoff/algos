from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores_stack = []

        operators = {
            '+': lambda stk: stk.append(stk[-2] + stk[-1]),
            'D': lambda stk: stk.append(stk[-1] * 2),
            'C': lambda stk: stk.pop(),
        }

        for element in ops:
            if element in operators:
                operators[element](scores_stack)
                continue
            scores_stack.append(int(element))
        return sum(scores_stack)
