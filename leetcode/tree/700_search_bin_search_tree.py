# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack = []
        if not root or root.val == val:
            return root

        if root.val > val:
            node = root.left
        else:
            node = root.right

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val == val:
                return node
            node = node.right
        return None

class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return node
        return None
