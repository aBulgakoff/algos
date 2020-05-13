from collections import deque


class Solution:  # O(N) time, O(N) space # Greedy
    def removeKdigits(self, nums: str, k: int) -> str:
        digits = deque()
        
        for d in map(int, nums):
            while k and digits and digits[-1] > d:
                digits.pop()
                k -= 1
            digits.append(d)

        while k:
            digits.pop()
            k -= 1

        while digits and not digits[0]:
            digits.popleft()

        return ''.join(map(str, digits)) or '0'
