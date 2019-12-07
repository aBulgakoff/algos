from collections import deque
from typing import List

import pytest

test_data = [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2, [1, 3]),
    ([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 1, 2, [1]),
    ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4]),
    ([1, 2], 1, 1, [1]),
    ([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4, [0, 1, 1, 1, 2, 3, 6, 7, 8])
]


@pytest.mark.parametrize('arr, k, x, output', test_data)
def test_find_closest(arr, k, x, output):
    assert Solution().findClosestElements(arr, k, x) == output


@pytest.mark.parametrize('arr, k, x, output', test_data)
def test_find_closest_small(arr, k, x, output):
    assert SolutionSmall().findClosestElements(arr, k, x) == output


class SolutionSmall:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def bin_search(left, right):
            if left < right:
                pivot = (left + right) // 2
            else:
                return left

            if (x - arr[pivot]) > (arr[pivot + k] - x):
                return bin_search(pivot + 1, right)
            else:
                return bin_search(left, pivot)

        start_index = bin_search(0, len(arr) - k)
        return arr[start_index:start_index + k]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        last_element_arr = len(arr) - 1

        def bin_search_first(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            else:
                return left

            if arr[pivot] == x:
                if arr[pivot - 1] != x:
                    return pivot
                else:
                    return bin_search_first(left, pivot)
            elif arr[pivot] > x:
                return bin_search_first(left, pivot)
            else:
                return bin_search_first(pivot, right)

        def bin_search_last(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            else:
                return right

            if arr[pivot] == x:
                if arr[pivot + 1] != x:
                    return pivot
                else:
                    return bin_search_last(pivot, right)
            elif arr[pivot] > x:
                return bin_search_last(left, pivot)
            else:
                return bin_search_last(pivot, right)

        if arr[0] > x:
            indexes_around_pivot = 0, 0
        elif arr[last_element_arr] < x:
            indexes_around_pivot = last_element_arr, last_element_arr
        else:
            indexes_around_pivot = bin_search_first(0, last_element_arr), bin_search_last(0, last_element_arr)

        if (x - arr[indexes_around_pivot[0]]) <= abs(x - arr[indexes_around_pivot[1]]):
            pivot_index = indexes_around_pivot[0]
        else:
            pivot_index = indexes_around_pivot[1]

        left_index, right_index = pivot_index - 1, pivot_index + 1

        results = deque([arr[pivot_index]])

        def get_element(index):
            if 0 <= index <= last_element_arr:
                return arr[index]
            else:
                raise IndexError(f'Index {index} out of range 0:{last_element_arr}')

        for number in range(k - 1):  # one number (pivot itself) already in results
            try:
                left_element = get_element(left_index)
            except IndexError:  # exception is risen when no elements left on left side
                results.append(get_element(right_index))
                right_index += 1
                continue

            try:
                right_element = get_element(right_index)
            except IndexError:  # exception is risen when no elements left on right side
                results.appendleft(get_element(left_index))
                left_index -= 1
                continue

            # take closer to target element with priority of left ones
            if (x - left_element) <= abs(x - right_element):
                results.appendleft(left_element)
                left_index -= 1
            else:
                results.append(right_element)
                right_index += 1
        return list(results)
