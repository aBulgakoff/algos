from typing import List

import pytest

test_data = [
    ([1, 2, 3, 1], (2,)),
    ([1, 2, 1, 3, 5, 6, 4], (1, 5)),

    ([1, 2, 3, 4, 3], (3,)),
    ([3, 4, 3, 2, 1], (1,)),

    ([1, 2, 3, 4, 3, 4], (3, 5)),
    ([2, 3, 2, 1, 2, 3, 4, 8], (1, 7)),

    ([1, 2, 1, 2], (1, 3)),
    ([1, 2, 3, 4], (3,)),
    ([1, 2, 3, 4, 5], (4,)),
    ([4, 3, 2, 1], (0,)),
    ([2, 1, 2, 1], (0, 2)),
    ([1, 2], (1,)),

]


@pytest.mark.parametrize('nums, output', test_data)
def test_find_peak(nums, output):
    assert Solution().findPeakElement(nums) in output


@pytest.mark.parametrize('nums, output', test_data)
def test_find_peak_sol_two(nums, output):
    assert SolutionTwo().findPeakElement(nums) in output


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search(left, right):
            if left < right - 1:
                pivot = (left + right) // 2
            else:
                return left if nums[left] > nums[right] else right

            if nums[pivot - 1] < nums[pivot]:
                if nums[pivot] > nums[pivot + 1]:
                    return pivot  # found peak
                else:
                    return bin_search(pivot, right)  # peak could be by right side
            else:
                return bin_search(left, pivot)

        return bin_search(0, len(nums) - 1)


class SolutionTwo:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        def bin_search(left, right):
            if left < right:
                pivot = (left + right) // 2
            else:
                return right

            if nums[pivot] > nums[pivot - 1]:
                if nums[pivot] > nums[pivot + 1]:
                    return pivot
                else:
                    return bin_search(pivot + 1, right)
            else:
                return bin_search(left, pivot)

        return bin_search(0, len(nums) - 1)
