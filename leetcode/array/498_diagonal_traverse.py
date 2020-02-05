from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        if not matrix or not matrix[0]:
            return result

        rows_amt, columns_amt = len(matrix), len(matrix[0])
        row, column = 0, 0

        is_direction_up = True

        while row < rows_amt and column < columns_amt:
            result.append(matrix[row][column])

            next_row = row + (-1 if is_direction_up else 1)
            next_column = column + (1 if is_direction_up else -1)

            if next_row < 0 or next_row == rows_amt or next_column < 0 or next_column == columns_amt:
                if is_direction_up:
                    # [i, j + 1] else [i + 1, j]
                    row += (column == columns_amt - 1)
                    column += (column < columns_amt - 1)
                else:
                    # [i + 1, j] else [i, j + 1]
                    column += (row == rows_amt - 1)
                    row += (row < rows_amt - 1)
                is_direction_up = not is_direction_up
            else:
                row = next_row
                column = next_column
        return result
