# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        ix_root_val = len(nums) // 2
        root_node = TreeNode(nums[ix_root_val])
        root_node.left = self.sortedArrayToBST(nums[:ix_root_val])
        root_node.right = self.sortedArrayToBST(nums[ix_root_val + 1:])
        return root_node


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        root = TreeNode(0)
        node, stack = root, []
        l, r = 0, len(nums)

        while l < len(nums):
            while l < r:
                stack.append((node, l, r))
                r = (l + r) // 2
                if l >= r:
                    break
                node.left = TreeNode(0)
                node = node.left

            node, l, r = stack.pop()
            m = (l + r) // 2
            node.val = nums[m]
            l = m + 1
            if l < r:
                node.right = TreeNode(0)
                node = node.right

        return root
