from collections import Counter


class Solution:     # O(N)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        return all(map(lambda ch: mc.get(ch, 0) >= rc[ch], rc))


class Solution2:    # O(N)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        bal = Counter(magazine)
        for ch in ransomNote:
            bal[ch] -= 1
        return all(qty >= 0 for qty in bal.values())


class Solution3:    # O(nlogn) # didn't try
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = sorted(ransomNote)
        mag = sorted(magazine)
        ir = im = 0
        while ir < len(ran) and im < len(mag):
            if ran[ir] == mag[im]:
                ir += 1
                im += 1
            elif ran[ir] > mag[im]:
                im += 1
            else:
                return False
        return ir == len(ran)
