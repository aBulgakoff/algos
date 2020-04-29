from collections import OrderedDict, Counter
from typing import List


class FirstUnique(Counter, OrderedDict):

    def __init__(self, nums: List[int]):
        self.nums = nums
        super().__init__(nums)

    def showFirstUnique(self) -> int:
        for key in self:
            if self[key] == 1:
                return key
        return -1

    def add(self, value: int) -> None:
        self[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
