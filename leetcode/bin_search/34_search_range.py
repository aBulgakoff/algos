from typing import List

import pytest

test_data = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),

    ([1], 1, [0, 0]),
    ([1, 2], 1, [0, 0]),
    ([1, 2, ], 2, [1, 1]),

    ([1], 2, [-1, -1])
]


@pytest.mark.parametrize('nums, target, output', test_data)
def test_search_range(nums, target, output):
    assert Solution().searchRange(nums, target) == output


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def first_appearance_search(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

            if nums[pivot] == target:
                if nums[pivot - 1] < target:
                    return pivot
                else:
                    return first_appearance_search(left, pivot - 1)
            elif nums[pivot] < target:
                return first_appearance_search(pivot, right)
            else:
                return first_appearance_search(left, pivot)

        def last_appearance_search(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            elif nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return -1

            if nums[pivot] == target:
                if nums[pivot + 1] > target:
                    return pivot
                else:
                    return last_appearance_search(pivot + 1, right)
            elif nums[pivot] < target:
                return last_appearance_search(pivot, right)
            else:
                return last_appearance_search(left, pivot)

        first_target_appearance = first_appearance_search(0, len(nums) - 1)
        last_target_appearance = last_appearance_search(first_target_appearance, len(nums) - 1)

        return [first_target_appearance, last_target_appearance]
