# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(parent, i, node, val):
            if not node:
                return
            if node.val == val:
                return i, parent
            return dfs(node, i + 1, node.left, val) or dfs(node, i + 1, node.right, val)

        x_index, x_parent = dfs(None, 0, root, x)
        y_index, y_parent = dfs(None, 0, root, y)
        return x_index == y_index and x_parent != y_parent
