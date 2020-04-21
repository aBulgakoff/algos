from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root_node = TreeNode(preorder[0])
        stack = [root_node]
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and val > stack[-1].val:
                    previous = stack.pop()
                previous.right = node
            stack.append(node)
        return root_node


class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack = deque((root := TreeNode(preorder[0]),))
        for node in map(TreeNode, preorder[1:]):
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and node.val > stack[-1].val:
                    previous = stack.pop()
                previous.right = node
            stack.append(node)
        return root
