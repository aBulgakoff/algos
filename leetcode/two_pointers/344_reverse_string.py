from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_index, right_index = 0, len(s) - 1
        while left_index < right_index:
            s[left_index], s[right_index] = s[right_index], s[left_index]
            left_index += 1
            right_index -= 1
