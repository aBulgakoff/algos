from collections import deque


class KeyNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.key == o.key
        return self.key == o

    def __hash__(self) -> int:
        return self.key.__hash__()


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._key_seed = 839
        self._storage = [deque() for _ in range(self._key_seed)]

    def _hash(self, key):
        return key % self._key_seed

    def _get_container(self, key):
        return self._storage[self._hash(key)]

    def _get_key_node(self, key):
        container = self._get_container(key)
        return container[container.index(key)]

    def _is_in(self, key):
        return self._get_container(key).__contains__(key)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if self._is_in(key):
            self._get_key_node(key).value = value
        else:
            self._get_container(key).append(KeyNode(key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self._is_in(key):
            return self._get_key_node(key).value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self._is_in(key):
            container = self._get_container(key)
            del container[container.index(key)]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)