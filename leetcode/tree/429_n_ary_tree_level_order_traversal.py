"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = deque([root]) if root else deque()

        while queue:
            current_level_size = len(queue)
            result.append(current_level := [])

            for _ in range(current_level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.children:
                    queue.extend(node.children)

        return result
