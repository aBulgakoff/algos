class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for symbol in S:
            if stack and stack[-1] == symbol:
                stack.pop()
                continue
            stack.append(symbol)

        return ''.join(stack)
