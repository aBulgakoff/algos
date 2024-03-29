# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def swap(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            all((swap(node.left), swap(node.right)))
            return node

        return swap(root)
