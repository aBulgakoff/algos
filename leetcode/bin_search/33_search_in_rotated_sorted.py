from bisect import bisect_left
from typing import List

import pytest

test_data = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),

    ([4, 5, 6, 7, 8, 9, 3], 3, 6),
    ([11, 5, 6, 7, 8, 9, 10], 11, 0),

    ([4, 5, 6, 7, 8, 9, 10], 6, 2),
    ([4, 5, 6, 7, 8, 9, 10], 10, 6),
    ([4, 5, 6, 7, 8, 9, 10], 4, 0),

    ([4, 5, 6, 7, 8, 9, 10], 3, -1),
    ([4, 5, 6, 7, 8, 9, 10], 11, -1),
    ([4, 5, 6, 7, 8, 9, 10], 100, -1),

    ([], 5, -1),
    ([5], 5, 0),
    ([4, 5], 5, 1),
    ([4, 5], 4, 0),
    ([5, 4], 4, 1),
    ([5, 4], 5, 0)
]


@pytest.mark.parametrize('nums, target, output', test_data)
def test_bin_search_rotation(nums, target, output):
    assert Solution().search(nums, target) == output


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or not str(target):
            return -1

        def rotation_point_search(left, right):
            if left < right - 1:
                pivot = (left + right) // 2
            else:
                return right if nums[right] < nums[left] else left

            if nums[left] > nums[pivot]:
                return rotation_point_search(left, pivot)
            else:
                return rotation_point_search(pivot, right)

        def bin_search(left, right):
            if left < right:
                pivot = (left + right) // 2
            else:
                return left if nums[left] == target else right

            if nums[pivot] < target:
                return bin_search(pivot + 1, right)
            elif nums[pivot] > target:
                return bin_search(left, pivot - 1)
            else:
                return pivot

        left, right = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            rotation_index = rotation_point_search(left, right)

            if nums[0] <= target <= nums[rotation_index - 1]:
                right = rotation_index - 1
            elif nums[rotation_index] <= target <= nums[-1]:
                left = rotation_index
            else:
                return -1  # target > max(nums)

        result_target = bin_search(left, right)
        return result_target if nums[result_target] == target else -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        index, left, right = 0, 0, len(nums) - 1
        if not nums:
            return -1

        while left < right - 1:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid

        if nums[-1] < target or nums[0] < nums[-1]:
            index = bisect_left(nums, target, hi=right)
        else:
            index = bisect_left(nums, target, lo=right)
        return index if nums[index] == target else -1
