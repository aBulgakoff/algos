# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = float('-inf')

        def path_sum(node):
            if not node:
                return 0

            left_pot = max(path_sum(node.left), 0)
            right_pot = max(path_sum(node.right), 0)
            pot_path = node.val + left_pot + right_pot

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, pot_path)
            return node.val + max(left_pot, right_pot)

        path_sum(root)
        return max_path_sum
