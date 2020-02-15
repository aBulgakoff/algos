"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def link_three_nodes(left_node, node, right_node):
    left_node.next = node
    node.next = right_node


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node

        cursor = head.next
        min_node, max_node = None, None
        while True:
            if cursor.val > cursor.next.val:
                max_node, min_node = cursor, cursor.next
                break
            if cursor is head:
                break
            cursor = cursor.next

        if min_node and max_node:
            if insertVal >= max_node.val or insertVal <= min_node.val:
                link_three_nodes(max_node, new_node, min_node)
            else:
                cursor = min_node
                while True:
                    if cursor.val <= insertVal <= cursor.next.val:
                        link_three_nodes(cursor, new_node, cursor.next)
                        break
                    cursor = cursor.next
        else:
            link_three_nodes(head, new_node, head.next)
        return head


class Solution2:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        cursor = head.next
        min_node, max_node = None, None
        while True:
            if cursor.val <= insertVal <= cursor.next.val:
                link_three_nodes(cursor, new_node, cursor.next)
                break
            if cursor.val > cursor.next.val:
                max_node, min_node = cursor, cursor.next
                if insertVal >= max_node.val or insertVal <= min_node.val:
                    link_three_nodes(max_node, new_node, min_node)
                    break
            if cursor is head:
                link_three_nodes(head, new_node, head.next)
                break
            cursor = cursor.next
        return head
