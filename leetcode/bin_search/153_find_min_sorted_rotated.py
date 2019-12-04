from typing import List

import pytest

test_data = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([], -1),
    ([3, 1, 2], 1),
    ([3, 1, 0], 0)
]


@pytest.mark.parametrize('input, output', test_data)
def test_find_min(input, output):
    assert Solution().findMin(input) == output


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        def bin_search(left, right):
            if left < right - 1:
                pivot = (left + right) // 2
            else:
                return right if nums[right] < nums[left] else left

            if nums[left] < nums[pivot]:
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    return bin_search(pivot, right)
            else:
                if nums[pivot - 1] > nums[pivot]:
                    if nums[pivot] < nums[pivot + 1]:
                        return pivot
                    else:
                        return bin_search(pivot, right)
                else:
                    return bin_search(left, pivot)

        if nums[0] < nums[-1]:
            return nums[0]  # rotation does not exist
        else:
            return nums[bin_search(0, len(nums) - 1)]
