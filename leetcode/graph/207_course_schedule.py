from collections import defaultdict
from itertools import repeat
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = defaultdict(list)
        self.visited = list(repeat(0, numCourses))

        for c, d in prerequisites:
            self.adj[c].append(d)

        for c in range(numCourses):
            if not self.visited[c] and not self.dfs(c):
                return False
        return True

    def dfs(self, c):
        if self.visited[c] == 1:
            return False
        self.visited[c] = 1
        if not all(map(self.dfs, self.adj[c])):
            return False

        self.visited[c] = 2

        return True
