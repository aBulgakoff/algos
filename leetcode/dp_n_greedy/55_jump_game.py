from typing import List


class Solution:  # greedy
    def canJump(self, nums: List[int]) -> bool:
        ix = prev_valid_pos = len(nums) - 1
        for num in reversed(nums):
            if ix + num >= prev_valid_pos:
                prev_valid_pos = ix
            ix -= 1
        return prev_valid_pos is 0
