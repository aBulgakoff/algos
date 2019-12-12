from itertools import chain
from typing import List


# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_array = []
        index = len(A) - 1
        while index >= 0:
            if A[index] % 2 != 0:
                even_array.append(A.pop(index))
            index -= 1
        return list(chain.from_iterable(zip(A, even_array)))
