from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        qty = sum(matrix[0])
        qty += sum((i[0] for i in matrix[1:]))

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] += min(matrix[i - 1][j],
                                        matrix[i][j - 1],
                                        matrix[i - 1][j - 1])
                    qty += matrix[i][j]

        return qty


class Solution2:  # clean but not obvious
    def countSquares(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))
