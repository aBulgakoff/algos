from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_no_element = 0
        for index, element in enumerate(nums):
            if element != val:
                nums[index_no_element] = element
                index_no_element += 1
        # can be nums = nums[:index_no_element + 1]
        return index_no_element
