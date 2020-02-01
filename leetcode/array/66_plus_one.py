from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''
        for digit in digits:
            digits_str += str(digit)

        return [int(digit) for digit in str(int(digits_str) + 1)]
