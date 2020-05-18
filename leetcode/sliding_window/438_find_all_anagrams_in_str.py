from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s < p:
            return list()

        result = []

        text = Counter()
        word = Counter(p)

        for i, ch in enumerate(s):
            text[ch] += 1
            if i >= len(p):
                text[s[i - len(p)]] -= 1
                if not text[s[i - len(p)]]:
                    del text[s[i - len(p)]]
            if text == word:
                result.append(i - len(p) + 1)
        return result
