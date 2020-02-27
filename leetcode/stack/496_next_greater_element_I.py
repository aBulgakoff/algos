from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = dict.fromkeys(nums1, -1)

        for index, element in enumerate(nums2):
            if element in results:
                for next_element in nums2[index:]:
                    if next_element > element:
                        results[element] = next_element
                        break

        return [results[element] for element in nums1]


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count_elems = {}

        for element in nums2:
            while stack:
                if element > stack[-1]:
                    count_elems[stack.pop()] = element
                else:
                    break
            stack.append(element)

        count_elems.update({key: -1 for key in stack})
        return [count_elems[element] for element in nums1]
