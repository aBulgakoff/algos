class Solution:
    def isValid(self, s: str) -> bool:
        validation_stack = []
        opening_parentheses = {'(', '{', '['}
        closing_parentheses = {')':'(', '}':'{', ']':'['}

        for symbol in s:
            if symbol in opening_parentheses:
                validation_stack.append(symbol)
            elif symbol in closing_parentheses:
                if not validation_stack or validation_stack[-1] != closing_parentheses[symbol]:
                    return False
                else:
                    validation_stack.pop(-1)
        return not validation_stack
