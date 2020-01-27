from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
