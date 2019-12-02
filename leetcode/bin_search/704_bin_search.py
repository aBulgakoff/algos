from typing import List

import pytest

data_set = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([1, 2], 2, 1),
    ([1, 2], 1, 0),
    ([1], 1, 0),
    ([1], 2, -1),
    ([], 4, -1),
    (None, 5, -1),

    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([-1, 0, 3, 5, 9, 12], 13, -1)
]


@pytest.mark.parametrize('nums, target, output', data_set)
def test_bin_search(nums, target, output):
    assert Solution().search(nums, target) == output


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def bin_search(left, right):
            if left < right:
                pivot = (right + left) // 2
            else:
                return left if nums[left] == target else right

            if nums[pivot] < target:
                return bin_search(pivot + 1, right)
            elif nums[pivot] > target:
                return bin_search(left, pivot - 1)
            else:
                return pivot

        index = bin_search(0, len(nums) - 1)
        return index if nums[index] == target else -1
