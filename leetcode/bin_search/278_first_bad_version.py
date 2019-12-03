import pytest

test_data = [
    ([0, 0, 0, 1, 1], 4),
    ([0, 0, 0, 0, 1], 5),
    ([0, 1, 1, 1, 1], 2),

    ([1, 1, 1, 1, 1], 1),
    ([0, 0, 0, 0, 0], -1),
    ([0], -1),
    ([1], 1),
    ([], -1),
]


@pytest.mark.parametrize('data, output', test_data)
def test_bin_search(data, output):
    global versions_history
    versions_history = data
    assert Solution().firstBadVersion(len(data)) == output


def isBadVersion(version: int) -> bool:
    return bool(versions_history[version - 1])


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n < 1:
            return -1

        def bin_search(left, right):
            if left < right -1:
                pivot = (left + right) // 2
            elif isBadVersion(left):
                return left
            elif isBadVersion(right):
                return right
            else:
                return -1

            is_bad_version = isBadVersion(pivot)

            if is_bad_version:
                if pivot > 1:
                    return bin_search(left, pivot - 1) if isBadVersion(pivot - 1) else pivot
                else:
                    return pivot
            else:
                return bin_search(pivot, right)

        return bin_search(1, n)
