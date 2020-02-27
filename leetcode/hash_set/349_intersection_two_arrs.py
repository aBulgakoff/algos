from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums2 = set(nums2)
        return list(set(filter(snums2.__contains__, nums1)))
