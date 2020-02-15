from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous_row = []
        row = []
        for row_num in range(rowIndex + 1):
            previous_row, row = row, [1 for _ in range(row_num + 1)]
            for col in range(1, len(row) - 1):
                row[col] = previous_row[col - 1] + previous_row[col]
        return row
