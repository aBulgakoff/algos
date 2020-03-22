# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        self.node = self.stack.pop()
        node_value = self.node.val
        self.node = self.node.right
        return node_value

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.node

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
