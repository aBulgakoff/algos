from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        resource_ix = count = 0
        if not s:
            return count
        g.sort()
        s.sort()
        for need in g:
            try:
                while need > s[resource_ix]:
                    resource_ix += 1
                else:
                    count += 1
                    resource_ix += 1
            except IndexError:
                break
        return count


class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child_ix = cookie_ix = 0
        g.sort()
        s.sort()
        while cookie_ix < len(s) and child_ix < len(g):
            if s[cookie_ix] >= g[child_ix]:
                child_ix += 1
            cookie_ix += 1
        return child_ix
