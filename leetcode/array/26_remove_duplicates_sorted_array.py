from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        last_number = nums[0]
        slow_index = 1
        for index in range(1, len(nums)):
            if last_number != nums[index]:
                nums[slow_index] = nums[index]
                last_number = nums[index]
                slow_index += 1
        return slow_index
