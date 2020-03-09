import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        priority = {}
        for key in nums:
            priority[key] = priority.get(key, 0) + 1
        return sorted(priority.keys(), key=lambda x: priority[x])[-1:-(k + 1):-1]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        priority = {}
        for key in nums:
            priority[key] = priority.get(key, 0) + 1
        return heapq.nlargest(k, priority, key=priority.get)
