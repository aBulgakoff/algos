"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:  # reversed pre-order
    def postorder(self, root: 'Node') -> List[int]:
        stack, result = [root], []
        while stack and stack[-1]:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                stack.extend(node.children)  # reverse child order
        return result[::-1]  # reverse result


class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        stack, result, visited_nodes = [root], [], set()
        while stack and stack[-1]:
            node = stack[-1]
            if node in visited_nodes:
                stack.pop()
                result.append(node.val)
            else:
                stack.extend(node.children[::-1])
            visited_nodes.add(node)
        return result
