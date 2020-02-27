from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashed = {element: index for index, element in enumerate(nums)}
        for ix, num in enumerate(nums):
            if target - num in nums_hashed:
                if ix != (snd_ix := nums_hashed[target - num]):
                    return [ix, snd_ix] if ix < snd_ix else [snd_ix, ix]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashed = {}
        for ix, num in enumerate(nums):
            if target - num in nums_hashed:
                if ix != (snd_ix := nums_hashed[target - num]):
                    return sorted([ix, snd_ix])
            nums_hashed[num] = ix
