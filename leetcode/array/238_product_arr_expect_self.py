from itertools import accumulate
from operator import mul
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [l * r
                for l, r
                in zip(accumulate(nums, mul, initial=1),
                       list(accumulate(reversed(nums), mul, initial=1))[len(nums) - 1::-1])]


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [*accumulate(nums[::-1], mul, initial=1)][len(nums) - 1::-1]
        product[:] = map(mul, product, accumulate(nums, mul, initial=1))
        return product


class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = right_prod = 1
        product = [1 for _ in nums]
        for i in range(len(nums)):
            product[i] *= left_prod
            left_prod *= nums[i]

            product[-1 - i] *= right_prod
            right_prod *= nums[-1 - i]
        return product
