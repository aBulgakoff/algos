from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(level, node):
            if not node or level >= len(arr) or node.val != arr[level]:
                return False
            if level == len(arr) - 1 and node.val == arr[-1] and not any((node.left, node.right)):
                return True
            return any((dfs(level + 1, node.left), dfs(level + 1, node.right)))

        return dfs(0, root)
