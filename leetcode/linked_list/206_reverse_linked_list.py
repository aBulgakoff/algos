# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cursor = head
        previous_node = next_cursor = None

        while cursor:
            next_cursor = cursor.next
            cursor.next = previous_node  # actual re-link
            previous_node = cursor
            cursor = next_cursor
        return previous_node
