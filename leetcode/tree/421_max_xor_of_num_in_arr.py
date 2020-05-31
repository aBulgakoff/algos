from collections import defaultdict
from functools import reduce
from typing import List

Trie = lambda: defaultdict(Trie)


class Solution: # from solutions
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        nums[:] = ([(x >> i) & 1 for i in range(L)][::-1] for x in nums)
        node = Trie()

        for num in nums:
            reduce(dict.__getitem__, num, node)['.'] = num

        max_xor = 0
        for num in nums:
            xor_node = node
            curr_xor = 0
            for bit in num:
                opp_bit = 1 - bit
                if opp_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[opp_bit]
                else:
                    curr_xor <<= 1
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor
