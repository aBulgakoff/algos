# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_parent_node(root_node, value):
    node = parent_node = root_node
    while node.val != value:
        parent_node = node
        if node.val < value:
            node = getattr(node, node_slot := 'right')
        else:
            node = getattr(node, node_slot := 'left')
    return parent_node, node_slot


def find_successor_parent(root_node):
    parent_node = root_node
    node = getattr(parent_node, successor_slot := 'right')
    while node.left:
        parent_node = node
        node = getattr(node, successor_slot := 'left')
    return parent_node, successor_slot


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        sentinel_node = TreeNode(float('-inf'))
        sentinel_node.right = root

        try:
            parent_node, node_slot = find_parent_node(sentinel_node, key)
        except AttributeError:
            pass  # key not found in the tree
        else:
            target_node = getattr(parent_node, node_slot)

            if not target_node.right:
                setattr(parent_node, node_slot, target_node.left)
            else:
                successor_parent_node, successor_slot = find_successor_parent(target_node)
                successor_node = getattr(successor_parent_node, successor_slot)

                target_node.val = successor_node.val
                setattr(successor_parent_node, successor_slot, successor_node.right)
        return sentinel_node.right
