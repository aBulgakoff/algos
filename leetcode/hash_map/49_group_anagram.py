from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        for element in strs:
            sorted_element = ''.join(sorted(element))
            storage[sorted_element] = storage.get(sorted_element, []) + [element]
        return [*storage.values()]
