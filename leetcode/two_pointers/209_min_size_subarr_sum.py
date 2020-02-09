from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        nums_sum = 0
        min_sub_len = 0
        left_index = 0
        sum_dict = {}

        for index, element in enumerate(nums):
            nums_sum += element
            sum_dict[index] = nums_sum
            if not min_sub_len and nums_sum >= s:
                min_sub_len = index + 1

        if not min_sub_len:
            return 0

        for index, element in enumerate(nums):
            if sum_dict[index] - sum_dict[left_index] >= s:
                min_sub_len = min(min_sub_len, index - left_index)
                while sum_dict[index] - sum_dict[left_index + 1] >= s:
                    left_index += 1
                    min_sub_len = min(min_sub_len, index - left_index)

        return min_sub_len


class Solution2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum_nums = 0
        left_index = 0
        sub_len = len(nums) + 1

        for index, element in enumerate(nums):
            sum_nums += element
            while sum_nums >= s:
                sub_len = min(sub_len, index + 1 - left_index)
                sum_nums -= nums[left_index]
                left_index += 1
        return sub_len if sub_len <= len(nums) else 0
