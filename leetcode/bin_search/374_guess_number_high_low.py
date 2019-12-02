import pytest

tests = (
    ([1, 1, 1, 1, 1, 0, -1, -1, -1, -1], 6),
    ([0, -1, -1, -1, -1, -1, -1, -1, -1, -1], 1),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 10),
    ([0], 1),
    ([0, -1], 1),
    ([1, 0], 2)
)


@pytest.mark.parametrize('data_set, output', tests)
def test_guess_number(data_set, output):
    global data
    data = data_set
    assert Solution().guessNumber(len(data_set)) == output


def guess(num: int) -> int:
    return data[num - 1]


class Solution:
    def guessNumber(self, n: int) -> int:

        def bin_search(left, right):
            if left < right:
                pivot = (left + right) // 2
            else:
                pivot = left

            response = guess(pivot)

            if response == -1:
                return bin_search(left, pivot - 1)
            elif response == 1:
                return bin_search(pivot + 1, right)
            else:
                return pivot

        return bin_search(1, n)
