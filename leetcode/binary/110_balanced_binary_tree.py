# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        stack, node, previous_node, depths = [], root, None, {}
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if not node.right or previous_node is node.right:
                node = stack.pop()
                left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                previous_node = node
                node = None
            else:
                node = node.right
        return True
