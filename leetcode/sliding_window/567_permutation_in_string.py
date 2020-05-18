from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word = Counter(s1)
        w_len = len(s1)

        fragm = Counter()
        perm = 0

        for i, ch in enumerate(s2):
            fragm[ch] += 1

            if i >= w_len:
                fragm[(l_ch := s2[i - w_len])] -= 1
                if not fragm[l_ch]:
                    del fragm[l_ch]

            perm += fragm == word

        return perm
