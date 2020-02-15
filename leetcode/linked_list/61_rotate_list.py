# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        cursor = head
        size = 0
        while cursor:
            size += 1
            cursor = cursor.next
        qty_rotation = k % size  # rotate less than size

        cursor = slow_cursor = head
        for qty in range(qty_rotation):
            cursor = cursor.next
        while cursor.next:
            slow_cursor = slow_cursor.next
            cursor = cursor.next

        cursor.next = head  # link last element with old head
        head = slow_cursor.next  # re-assign head
        slow_cursor.next = None  # set last element

        return head
