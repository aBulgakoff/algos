# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return list()
            return dfs(node.left) + [node.val] + dfs(node.right)

        return dfs(root)[k - 1]
