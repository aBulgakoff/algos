from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        left_ix, right_ix = 0, len(nums) - 1
        left_sum, right_sum = nums[left_ix], nums[right_ix]

        while left_ix < right_ix - 1:
            if left_sum <= right_sum:
                left_ix += 1
                left_sum += nums[left_ix]
            else:
                right_ix -= 1
                right_sum += nums[right_ix]

        while left_sum <= right_sum and left_ix != right_ix:
            left_ix += 1
            right_ix -= 1
            left_sum += nums[left_ix]
            right_sum -= nums[right_ix]
        return nums[:left_ix + 1]


class Solution2:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        left_sum, right_sum = 0, sum(nums)
        for ix, num in enumerate(nums):
            right_sum -= num
            left_sum += num
            if left_sum > right_sum:
                return nums[:ix + 1]
