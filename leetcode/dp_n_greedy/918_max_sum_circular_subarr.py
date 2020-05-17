def find_max(nums: List[int]) -> int:
    local_max = global_max = nums[0]
    for num in nums[1:]:
        local_max = max(num, local_max + num)
        global_max = max(global_max, local_max)
    return global_max


class Solution:  # greedy # Kadane's algorithm # O(n) time 0(1) space
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        positive = find_max(A)
        negative = find_max([-num for num in A]) + sum(A)

        if negative and negative > positive:
            return negative
        return positive


class Solution2:
    # greedy # Kadane's algorithm # O(1n) time 0(1) space
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        local_max = global_max = local_min = global_min = accum = A[0]
        for num in A[1:]:
            local_max = max(num, local_max + num)
            global_max = max(local_max, global_max)

            local_min = min(num, local_min + num)
            global_min = min(local_min, global_min)

            accum += num

        return max((accum - global_min) or global_max, global_max)
