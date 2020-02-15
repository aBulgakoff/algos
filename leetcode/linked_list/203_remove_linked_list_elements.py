# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel_node = ListNode(-1)
        sentinel_node.next = head

        slow_cursor, cursor = sentinel_node, sentinel_node.next
        while cursor:
            if cursor.val == val:
                slow_cursor.next = cursor.next
            else:
                slow_cursor = cursor
            cursor = cursor.next
        return sentinel_node.next
