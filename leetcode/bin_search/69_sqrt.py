import math

import pytest


@pytest.mark.parametrize('num', [num for num in range(10000)])
def test_bin_search(num):
    assert Solution().mySqrt(num) == int(math.sqrt(num))


class Solution:
    def mySqrt(self, x: int) -> int:
        def bin_search(left, right):
            if left <= right:
                pivot = (left + right) // 2
            else:
                return right if right * right < x else left

            pow2 = pivot * pivot

            if pow2 == x:
                return pivot
            elif pow2 > x:
                return bin_search(left, pivot - 1)
            else:
                return bin_search(pivot + 1, right)

        return bin_search(0, x)
