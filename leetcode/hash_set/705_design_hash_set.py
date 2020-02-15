from collections import deque


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_seed = 839
        self._storage = [deque() for _ in range(self.key_seed)]

    def _hash(self, key: int) -> int:
        return key % self.key_seed

    def add(self, key: int) -> None:
        key_hash = self._hash(key)
        if not self.contains(key):
            self._storage[key_hash].append(key)

    def remove(self, key: int) -> None:
        key_hash = self._hash(key)
        if self.contains(key):
            self._storage[key_hash].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        key_hash = self._hash(key)
        return self._storage[key_hash].__contains__(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
