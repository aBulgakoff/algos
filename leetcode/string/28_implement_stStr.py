class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        is_fully_matched = False
        try:
            for index in range(len(haystack)):
                if haystack[index] == needle[0]:
                    for i in range(len(needle)):
                        is_fully_matched = True
                        if haystack[index + i] != needle[i]:
                            is_fully_matched = False
                            break
                    if is_fully_matched:
                        return index
        except IndexError:
            is_fully_matched = False
        return -1
