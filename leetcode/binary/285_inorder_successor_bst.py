# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = [node := root]
        previous_node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if stack:
                previous_node = stack[-1]
            if node is p:
                if next_node := node.right:
                    while next_node.left:
                        next_node = next_node.left
                    return next_node
                if previous_node.val > p.val:
                    return previous_node
            node = node.right
        return None
