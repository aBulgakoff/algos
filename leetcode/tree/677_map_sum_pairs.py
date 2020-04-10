class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['val'] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        sum_val_children = 0

        try:
            for ch in prefix:
                node = node[ch]
        except KeyError:
            return sum_val_children

        stack = [node]
        while stack and stack[-1]:
            node = stack.pop()
            sum_val_children += node.get('val', 0)
            stack.extend(n for k, n
                         in node.items()
                         if k != 'val')
        return sum_val_children

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)