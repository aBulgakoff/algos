class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow_cursor, fast_cursor = head, head.next
        while slow_cursor is not fast_cursor:
            if not fast_cursor or not fast_cursor.next:
                return False
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
        return True
