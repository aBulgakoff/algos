from collections import Counter, OrderedDict


class Solution:
    def frequencySort(self, s: str) -> str:
        fr = OrderedDict(Counter(s))
        return ''.join(ch * fr[ch] for ch in sorted(fr, key=fr.get, reverse=True))


class Solution2:
    def frequencySort(self, s: str) -> str:
        fr = OrderedDict(Counter(s))
        return ''.join(map(lambda x: x * fr[x], sorted(fr, key=fr.get, reverse=True)))
