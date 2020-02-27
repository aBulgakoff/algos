from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict.pop(num)
            else:
                nums_dict[num] = 1
        return nums_dict.popitem()[0]


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
