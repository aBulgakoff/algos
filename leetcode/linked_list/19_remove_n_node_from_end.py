# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_cursor = fast_cursor = head

        try:
            for _ in range(n + 1):
                fast_cursor = fast_cursor.next
        except AttributeError:  # fast_cursor == None
            return head.next  # head is at -n position

        while fast_cursor:  # move fast to end of list, slow.next is at position -n
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next

        slow_cursor.next = slow_cursor.next.next
        return head
