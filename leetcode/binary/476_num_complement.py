class Solution:
    def findComplement(self, num: int) -> int:
        # bitmask has the same length as num and contains only ones 1...1
        bit_mask = (1 << num.bit_length()) - 1
        return bit_mask ^ num
