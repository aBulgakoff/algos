class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        slow_ix, fast_ix, len_substr, buffer = 0, 0, 0, {}
        while fast_ix <= len(s):
            if len(buffer) <= k:
                try:
                    buffer[s[fast_ix]] = fast_ix
                except IndexError:
                    pass
                len_substr = max(len_substr, fast_ix - slow_ix)
                fast_ix += 1
            else:
                if buffer[s[slow_ix]] == slow_ix:
                    buffer.pop(s[slow_ix])
                slow_ix += 1
        return len_substr
