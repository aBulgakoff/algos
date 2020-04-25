from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_len = begin = 0
        pos = {}
        for index, ch in enumerate(s):
            begin = max(begin, pos.get(ch, 0))
            subs_len = max(subs_len, index - begin + 1)
            pos[ch] = index + 1
        return subs_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_len = beginning = 0
        pos = Counter()
        for index, ch in enumerate(s):
            beginning = max(beginning, pos[ch])
            subs_len = max(subs_len, index + 1 - beginning)
            pos[ch] = index + 1
        return subs_len
