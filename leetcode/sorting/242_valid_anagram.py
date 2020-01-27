import pytest

test_data = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("", "aa", False)
]


@pytest.mark.parametrize("s, t, result", test_data)
def test_is_anagram(s, t, result):
    assert Solution().isAnagram(s, t) == result


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}
        for character in s:
            result[character] = result.get(character, 0) + 1

        for character in t:
            result[character] = result.get(character, 0) - 1

        for character_count in result.values():
            if character_count:
                return False
        return True
