from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_operations = {
            '+': lambda num1, num2: num1 + num2,
            '-': lambda num1, num2: num1 - num2,
            '/': lambda num1, num2: int(num1 / num2),
            '*': lambda num1, num2: num1 * num2,
        }
        calc_stack = []
        for token in tokens:
            if token in math_operations:
                num2 = calc_stack.pop()
                num1 = calc_stack.pop()
                calc_stack.append(math_operations[token](num1, num2))
            else:
                calc_stack.append(int(token))
        return calc_stack.pop()
