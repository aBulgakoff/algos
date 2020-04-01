# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_stack_node(node: TreeNode, target_node: TreeNode) -> list:
    stack = [node]
    while node is not target_node:
        if node.val < target_node.val:
            node = node.right
        elif node.val > target_node.val:
            node = node.left
        stack.append(node)
    return stack


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_stack = get_stack_node(root, p)
        q_stack = get_stack_node(root, q)

        l_c_a = None
        for p_node, q_node in zip(p_stack, q_stack):
            if p_node is not q_node:
                break
            l_c_a = p_node
        return l_c_a
