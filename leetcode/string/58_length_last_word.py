class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s[::-1].split()[0].strip())


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        word_end = len(s) - 1
        while s[word_end] == " ":
            word_end -= 1

        word_len = 0
        word_start = word_end
        while word_start >= 0:
            if s[word_start] == " ":
                break
            word_len += 1
            word_start -= 1
        return word_len
