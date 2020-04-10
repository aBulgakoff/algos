"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from itertools import repeat


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth, stack = 0, []
        if root:
            stack.append((depth := depth + 1, root))

        while stack:
            current_depth, node = stack.pop()
            depth = max(depth, current_depth)

            if node.children:
                stack.extend(zip(repeat(current_depth + 1), node.children))
        return depth
