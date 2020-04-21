from functools import partial


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

def bin_search(verify, left, right):
    while left < right - 1:
        if verify(mid := (left + right) // 2):
            right = mid
        else:
            left = mid
    return left if verify(left) else right


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        leftmost_col = cols
        for row in range(rows):
            get_on_row = partial(binaryMatrix.get, row)
            col = bin_search(get_on_row, 0, cols - 1)
            if get_on_row(col):
                leftmost_col = min(leftmost_col, col)
        return leftmost_col if leftmost_col < cols else -1


class Solution2:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        leftmost_col = cols
        for row in range(rows):
            get_on_row = partial(binaryMatrix.get, row)
            col = bin_search(get_on_row, 0, cols - 1)
            if get_on_row(col):
                leftmost_col = min(leftmost_col, col)
        return leftmost_col if leftmost_col < cols else -1
