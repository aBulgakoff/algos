# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # reverse pre-order result
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:  # change left and right order
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # reverse


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node, stack, result = root, [], []
        while node or stack:
            while node:
                # push right on to stack before current node
                if node.right:
                    stack.append(node.right)
                # push current node onto stack and move left
                stack.append(node)
                node = node.left

            node = stack.pop()

            # if current node's right is at the top of stack
            # means it is not yet processed
            if stack and stack[-1] is node.right:
                # pop its right from stack
                right_node = stack.pop()
                # push current node to stack to process it in future
                stack.append(node)
                # point current node to its right
                node = right_node
            else:
                # if curr is left most and doesn't have any right
                # or if its right has already been processed
                # process current and set it to None
                result.append(node.val)
                node = None
        return result


class Solution3:    # stack and set
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, postorder, result = [root], set(), []
        while stack and stack[-1]:
            node = stack[-1]
            if node.left and node.left not in postorder:
                stack.append(node.left)
            elif node.right and node.right not in postorder:
                stack.append(node.right)
            else:
                node = stack.pop()
                postorder.add(node)
                result.append(node.val)
        return result
