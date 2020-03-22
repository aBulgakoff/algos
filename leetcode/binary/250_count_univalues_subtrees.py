# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_unival_node(root, 0)
        return self.count

    def is_unival_node(self, node, val):
        if not node:
            return True
        if not all((self.is_unival_node(node.left, node.val),
                    self.is_unival_node(node.right, node.val))):
            return False
        self.count += 1
        return node.val == val
