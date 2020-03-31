class Solution:
    def reverse(self, x: int) -> int:
        capacity = 2**31
        sign = 1 if x > 0 else -1
        reversed_absx = int(str(abs(x))[::-1])
        if reversed_absx < capacity:
            return sign * reversed_absx
        return 0
