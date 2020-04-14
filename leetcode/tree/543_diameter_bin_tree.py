# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        stack, postorder, children_max_height = [root], {}, 0
        while stack and stack[-1]:
            node = stack[-1]  # check if children processed already
            if node.left and node.left not in postorder:
                stack.append(node.left)
            elif node.right and node.right not in postorder:
                stack.append(node.right)
            else:
                node = stack.pop()  # children are processed or no children, pop the stack
                left_height = postorder.get(node.left, 0)
                right_height = postorder.get(node.right, 0)
                postorder[node] = max(left_height, right_height) + 1  # 1 is node itself
                children_max_height = max(left_height + right_height,
                                          children_max_height)
        return children_max_height
