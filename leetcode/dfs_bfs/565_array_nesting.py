from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_set_len = -1
        seen = set()
        for i in range(len(nums)):
            n = i
            current_set_len = 0
            while nums[n] not in seen:
                n = nums[n]
                seen.add(n)
                current_set_len += 1
            max_set_len = max(max_set_len, current_set_len)
        return max_set_len
