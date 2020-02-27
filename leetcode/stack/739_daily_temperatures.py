from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for _ in range(len(T))]
        stack = []

        for index in range(len(T) - 1, -1, -1):
            while stack and T[index] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[index] = stack[-1] - index
            stack.append(index)
        return result
