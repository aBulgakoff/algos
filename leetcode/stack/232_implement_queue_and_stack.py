from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._storage = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._storage.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._storage.popleft()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._storage

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
