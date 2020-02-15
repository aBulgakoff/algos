from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        qty_rot = k % len(nums) if k > len(nums) else k

        buffer = deque(nums[-qty_rot:])
        for index in range(len(nums)):
            buffer.append(nums[index])
            nums[index] = buffer.popleft()


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        qty_rot = k % len(nums)
        nums[:] = nums[-qty_rot:] + nums[:-qty_rot]
