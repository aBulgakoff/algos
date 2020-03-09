from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        index1 = 0
        index2 = 0
        result = []

        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                result.append(nums1[index1])
                index1 += 1
                index2 += 1

        return result


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_symbol_appearance = {}
        nums2_symbol_appearance = {}
        result = {}

        for char in nums1:
            nums1_symbol_appearance[char] = nums1_symbol_appearance.get(char, 0) + 1

        for char in nums2:
            nums2_symbol_appearance[char] = nums2_symbol_appearance.get(char, 0) + 1

        for char in nums1_symbol_appearance.keys():
            if char in nums2_symbol_appearance:
                result[char] = min(nums1_symbol_appearance[char], nums2_symbol_appearance[char])

        return [key for key, value in result.items() for _ in range(value)]


class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_symbol_appearance = {}
        nums2_symbol_appearance = {}
        result = []

        for char in nums1:
            nums1_symbol_appearance[char] = nums1_symbol_appearance.get(char, 0) + 1

        for char in nums2:
            nums2_symbol_appearance[char] = nums2_symbol_appearance.get(char, 0) + 1

        for char in nums1_symbol_appearance.keys():
            if char in nums2_symbol_appearance:
                result.extend(char for _ in range(min(nums1_symbol_appearance[char], nums2_symbol_appearance[char])))

        return result


from collections import Counter
from itertools import chain


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        product = Counter(nums1) & Counter(nums2)
        return [*chain(*map(lambda char: (char for _ in range(product[char])), product))]
