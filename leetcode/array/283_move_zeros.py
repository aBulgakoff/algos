from collections import deque
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_buffer = deque()
        slow_index = 0

        for index, element in enumerate(nums):
            if element == 0:
                zero_buffer.append(element)
            else:
                nums[slow_index] = element
                slow_index += 1

        for index in range(slow_index, len(nums)):
            nums[index] = zero_buffer.popleft()
