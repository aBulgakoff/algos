class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_digits = {}
        for ix, digit in enumerate(s):
            s_digits[digit] = s_digits.get(digit, []) + [ix]

        t_digits = {}
        for ix, digit in enumerate(t):
            t_digits[digit] = t_digits.get(digit, []) + [ix]

        return sorted(s_digits.values()) == sorted(t_digits.values())
