from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        storage = {}
        for element in strings:
            ord_first = ord(element[0])
            key = tuple(map(lambda order: (order - ord_first) % 26, map(ord, element)))
            storage[key] = storage.get(key, []) + [element]
        return [*storage.values()]
