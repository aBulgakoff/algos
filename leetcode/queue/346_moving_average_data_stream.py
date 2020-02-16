from functools import reduce


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.storage = []

    def next(self, val: int) -> float:
        self.storage.append(val)
        qty = self.size if len(self.storage) >= self.size else len(self.storage)
        return reduce(lambda x, y: x + y, self.storage[0 - qty:]) / qty


from collections import deque


class MovingAverage2:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.storage = deque([0 for _ in range(size)])
        self.sum = 0
        self.qty_elements_processed = 0

    def next(self, val: int) -> float:
        self.sum = self.sum - self.storage.popleft() + val
        self.storage.append(val)
        self.qty_elements_processed += 1
        return self.sum / min(self.qty_elements_processed, self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
