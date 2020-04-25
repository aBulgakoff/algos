from collections import OrderedDict


class LRUCache(OrderedDict):  # OrderedDict

    def __init__(self, capacity: int):
        self.capacity = capacity
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        OrderedDict.__setitem__(self, key, value)
        if len(self) > self.capacity:
            self.popitem(last=False)

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
