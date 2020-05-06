from collections import Counter
from typing import List


class Solution:  # sorting O(nlogn) time, O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        num_appear = Counter(nums)
        return sorted(num_appear.items(), key=lambda x: x[1], reverse=True)[0][0]


class Solution2:  # sorting O(nlogn) time, O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class Solution3:  # O(n) time, O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        num_appear = Counter(nums)
        return max(num_appear, key=num_appear.get)


class Solution4:  # O(n) time, O(1) space # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        qty = candidate = 0

        for num in nums:
            if not qty:
                candidate = num
            qty += 1 if num == candidate else -1

        return candidate
