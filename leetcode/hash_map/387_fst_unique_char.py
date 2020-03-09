class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for ix, char in enumerate(s):
            if char_count[char] == 1:
                return ix
        return -1
