from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        for element in strs:
            sorted_element = ''.join(sorted(element))
            storage[sorted_element] = storage.get(sorted_element, []) + [element]
        return [*storage.values()]


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_key(text: str) -> str:
            return ''.join(sorted(text))

        groupped_words = defaultdict(list)
        for word in strs:
            groupped_words[hash_key(word)].append(word)
        return [*groupped_words.values()]
