from typing import List


class Solution:  # O(n) time, 0(1) space # brute force
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sentinel = val = float('-inf')
        count = 0
        nums.append(sentinel)

        for num in nums:
            if val != num:
                if count == 1:
                    return val
                val = num
                count = 1
            else:
                count += 1


class Solution2:  # O(logN) time, O(1) space # binary search
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                cl, cr = mid, mid + 1
            elif mid and nums[mid] == nums[mid - 1]:
                cl, cr = mid - 1, mid
            else:
                return nums[mid]

            if not len(nums[:cl]) % 2:
                left = cr + 1
            else:
                right = cl


class Solution3:  # O(logN) time, O(1) space # binary search # partner(xor) index # StefanPochmann
    # mid ^ 1 == (mid + 1 if mid % 2 == 0 else mid - 1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
