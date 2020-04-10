import heapq
from typing import List


class Solution:  # greedy
    def maxNumberOfApples(self, arr: List[int]) -> int:
        capacity, counter = 5000, 0
        heapq.heapify(arr)
        while arr and capacity - arr[0] >= 0:
            capacity -= heapq.heappop(arr)
            counter += 1
        return counter


class Solution:  # greedy
    def maxNumberOfApples(self, arr: List[int]) -> int:
        weight, capacity = 0, 5000
        for index, apple in enumerate(sorted(arr)):
            if weight + apple > capacity:
                return index
            weight += apple
        return len(arr)
