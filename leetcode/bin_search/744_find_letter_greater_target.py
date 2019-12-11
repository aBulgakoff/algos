from typing import List

import pytest

test_data = [
    (["c", "f", "j"], "c", "f"),
    (["c", "f", "j"], "a", "c"),
    (["c", "f", "j"], "d", "f"),

    (["c", "f", "j"], "g", "j"),

    (["c", "f", "j"], "j", "c"),
    (["c", "f", "j"], "k", "c"),
]


@pytest.mark.parametrize('letters, target, output', test_data)
def test_find_greatest_letter(letters, target, output):
    assert Solution().nextGreatestLetter(letters, target) == output


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        def bin_search(left, right):
            if left < right:
                pivot = (left + right) // 2
            else:
                return letters[left]

            if letters[pivot] <= target:
                if letters[pivot + 1] > target:
                    return letters[pivot + 1]
                else:
                    return bin_search(pivot, right)
            else:
                return bin_search(left, pivot)

        return bin_search(0, len(letters) - 1)
