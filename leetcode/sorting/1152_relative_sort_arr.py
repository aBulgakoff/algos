from typing import List

import pytest

test_data = [
    {'arr1': [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], 'arr2': [2, 1, 4, 3, 9, 6],
     'output': [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]},
]


@pytest.mark.parametrize('data', test_data)
def test_relative_sort_arr(data):
    assert Solution3().relativeSortArray(data['arr1'], data['arr2']) == data['output']


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        matching_elements = {arr2[index]: index for index in range(len(arr2))}
        arr1.sort(key=lambda element: matching_elements[element] if element in matching_elements else 1001 + element)
        return arr1


class Solution2:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        matching_elements = {element: index for index, element in enumerate(arr2)}
        arr1.sort(key=lambda element: matching_elements.get(element, 1001 + element))
        return arr1


class Solution3:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_elements = {}
        for element in arr1:
            count_elements[element] = count_elements.get(element, 0) + 1

        matching_elements_position = {}
        last_element_position = -1
        for element in arr2:
            last_element_position += count_elements[element]
            matching_elements_position[element] = last_element_position

        result = [0 for _ in range(last_element_position + 1)]
        additional_elements = []
        for element in reversed(arr1):
            if element in matching_elements_position:
                position_to_insert = matching_elements_position[element]
                result[position_to_insert] = element
                matching_elements_position[element] = position_to_insert - 1
            else:
                additional_elements.append(element)

        result.extend(sorted(additional_elements))
        return result
