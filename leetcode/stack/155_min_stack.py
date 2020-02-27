class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        self._data.append(x)
        self._min.append(min(self._min[-1], x) if self._min else x)

    def pop(self) -> None:
        if self._data:
            del self._data[-1]
            del self._min[-1]

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return self._min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
