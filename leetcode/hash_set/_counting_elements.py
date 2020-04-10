from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter, elements = 0, set(arr)
        for elem in arr:
            if elem + 1 in elements:
                counter += 1
        return counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique_nums = set(arr)
        return sum(1 for num in arr if num + 1 in unique_nums)
