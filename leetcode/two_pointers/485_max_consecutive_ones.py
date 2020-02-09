from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_amount = 0
        counter = 0
        for element in nums:
            if element == 1:
                counter += 1
                max_amount = max(max_amount, counter)
            else:
                counter = 0
        return max_amount
