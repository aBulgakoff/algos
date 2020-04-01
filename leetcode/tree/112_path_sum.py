# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = [(root, root.val)] if root else []

        while stack:
            node, sum_by_node = stack.pop()

            if node.left:
                stack.append((node.left, sum_by_node + node.left.val))
            if node.right:
                stack.append((node.right, sum_by_node + node.right.val))

            if not node.left and not node.right and sum_by_node == sum:
                return True

        return False
