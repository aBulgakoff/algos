class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ix_s = ix_t = found_chs = 0
        while ix_s < len(s) and ix_t < len(t):
            if s[ix_s] == t[ix_t]:
                found_chs += 1
                ix_s += 1
            ix_t += 1
        return found_chs == len(s)
