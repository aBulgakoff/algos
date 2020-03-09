class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set(J)
        return sum(map(j_set.__contains__, S))
