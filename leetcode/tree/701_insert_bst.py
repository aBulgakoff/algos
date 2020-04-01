# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        new_node = TreeNode(val)
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break
        return root or new_node
