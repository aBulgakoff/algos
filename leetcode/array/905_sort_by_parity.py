from typing import List


# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        index = len(A) - 1
        while index >= 0:
            if A[index] % 2 != 0:
                A.append(A.pop(index))
            index -= 1
        return A
