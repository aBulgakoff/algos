from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        group = {}
        for p, d in dislikes:
            adjacency[p].append(d)
            adjacency[d].append(p)

        def dfs(p, g):
            if p in group:
                return group[p] == g
            group[p] = g
            return all(dfs(peer, g ^ 1) for peer in adjacency[p])

        return all(map(lambda p: dfs(p, 0),
                       filter(lambda x: x not in group,
                              adjacency))
                   )
