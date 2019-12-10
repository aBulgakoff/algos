# Example 1:
#
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
#
# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
import sys

import pytest


class Reader:
    def __init__(self, input):
        self.input = input

    def get(self, index):
        try:
            return self.input[index]
        except IndexError:
            return 2147483647


test_data = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
]


@pytest.mark.parametrize('input, target, output', test_data)
def test_search_unknown_size(input, target, output):
    assert Solution().search(Reader(input), target) == output


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        def bin_search(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            elif reader.get(left) == target:
                return left
            elif reader.get(right) == target:
                return right
            else:
                return -1

            if reader.get(pivot) == target:
                return pivot
            elif reader.get(pivot) < target:
                if reader.get(pivot + 1) > target:
                    return -1
                else:
                    return bin_search(pivot, right)
            else:
                return bin_search(left, pivot)

        return bin_search(0, 2147483647)
