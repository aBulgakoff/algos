from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        index = 0
        while index <= len(nums) - 2:
            result += min(nums[index], nums[index + 1])
            index += 2

        return result


class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        [result := result + nums[i] for i in range(0, len(nums), 2)]
        return result


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([element for index, element in enumerate(sorted(nums)) if index % 2 == 0])
