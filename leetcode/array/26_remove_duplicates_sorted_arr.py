from typing import List

import pytest

test_data = [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3], 4),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 3], 4)
]


@pytest.mark.parametrize('nums, target', test_data)
def test_remove_dups(nums, target):
    assert Solution2().removeDuplicates(nums) == target


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = len(nums) - 1
        while index > 0:
            if nums[index] == nums[index - 1]:
                del nums[index]
            index -= 1
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = len(nums) - 1
        while index > 0:
            if nums[index] == nums[index - 1]:
                nonunique_element_index = index
                unique_element_index = index - 2
                try:  # nums is not default List implementation, it doesn't have negative index getters
                    while nums[nonunique_element_index] == nums[unique_element_index]:
                        unique_element_index -= 1
                except IndexError:
                    pass
                del nums[unique_element_index + 2:nonunique_element_index + 1]
                index = unique_element_index
            else:
                index -= 1
        return len(nums)
