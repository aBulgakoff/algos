from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left_sum = 0
        for index, element in enumerate(nums):
            if left_sum == (nums_sum - left_sum - element):
                return index
            left_sum += element
        return -1
