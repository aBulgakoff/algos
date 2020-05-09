import pytest

test_data = [
    (16, True),
    (14, False),

    (2, True),
    (1, True),
    (0, False),

    (4, True),
    (5, False),

]


@pytest.mark.parametrize('input, output', test_data)
def test_perfect_square(input, output):
    assert Solution().isPerfectSquare(input) is output


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not num:
            return False
        if num == 2 or num == 1:
            return True

        def bin_search(left, right):
            if left + 1 < right:
                pivot = (left + right) // 2
            elif left * left == num or right * right == num:
                return True
            else:
                return False

            pivot_pow2 = pivot * pivot
            if pivot_pow2 == num:
                return True
            elif pivot_pow2 < num:
                if (pivot + 1) * (pivot + 1) > num:
                    return False
                else:
                    return bin_search(pivot, right)
            else:
                return bin_search(left, pivot)

        return bin_search(0, num // 2)


class Solution2:    # O(logN) time, 0(1) space
    def isPerfectSquare(self, num: int) -> bool:
        if not num:
            return False
        elif num == 1:
            return True

        left, right = 2, num

        while left < right - 1:
            mid = (left + right) // 2

            if mid ** 2 > num:
                right = mid
            else:
                left = mid

        return any(map(lambda x: num == x ** 2, (left, right)))


class Solution3:  # O(logN) time, O(1) space # Newton's Method
    def isPerfectSquare(self, num: int) -> bool:
        if not num:
            return False
        elif num == 1:
            return True
        right = num // 2
        while right ** 2 > num:
            right = (right + num // right) // 2
        return right ** 2 == num
