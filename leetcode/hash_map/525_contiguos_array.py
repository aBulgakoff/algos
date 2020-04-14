from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_per_index = {0: -1}  # balance is 0 before nums[0]
        max_len = balance = 0
        for index, num in enumerate(nums):
            balance += 1 if num else -1

            if balance in balance_per_index:
                # if this balance already occurred
                # check how many elements ago
                max_len = max(max_len, index - balance_per_index[balance])
            else:
                balance_per_index[balance] = index

        return max_len
