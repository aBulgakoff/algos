from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda string: len(string))
        prefix = strs[0] if strs else ""

        for string in strs:
            min_pair_len = min(len(string), len(prefix))
            for index in range(min_pair_len):
                if prefix[index] != string[index]:
                    prefix = prefix[:index]
                    break
        return prefix
