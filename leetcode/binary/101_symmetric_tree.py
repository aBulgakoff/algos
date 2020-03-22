# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]

        while stack:
            left_node, right_node = stack.pop()
            try:
                if left_node.val != right_node.val:
                    return False
            except AttributeError:
                if left_node is not right_node:
                    return False
            else:
                stack.append((left_node.left, right_node.right))
                stack.append((left_node.right, right_node.left))
        return True
