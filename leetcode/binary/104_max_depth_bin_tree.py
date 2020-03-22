# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth, stack = 0, []
        stack.append((depth := 1, root)) if root else ''

        while stack:
            level, node = stack.pop()
            depth = max(depth, level)
            if node.left:
                stack.append((level + 1, node.left))
            if node.right:
                stack.append((level + 1, node.right))

        return depth
