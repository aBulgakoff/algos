# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = previous_node = ListNode(None)
        l1_cursor = l1
        l2_cursor = l2

        while l1_cursor and l2_cursor:
            if l1_cursor.val < l2_cursor.val:
                previous_node.next = l1_cursor
                l1_cursor = l1_cursor.next
            else:
                previous_node.next = l2_cursor
                l2_cursor = l2_cursor.next
            previous_node = previous_node.next
        previous_node.next = l1_cursor if l1_cursor else l2_cursor
        return new_head.next
