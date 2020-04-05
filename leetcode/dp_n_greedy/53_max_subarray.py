from typing import List


class Solution:  # greedy
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]
        for ix in range(1, len(nums)):
            local_max = max(local_max + nums[ix], nums[ix])
            global_max = max(global_max, local_max)
        return global_max
