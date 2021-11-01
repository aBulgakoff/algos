# Definition for singly-linked list.
from typing import Optional


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


class Solution2: # another vars names
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head

        while node:
            # memorize next step
            next_step = node.next

            # re-link current to prev
            node.next = prev

            # move cursor, current going to be prev, next step - current
            prev = node
            node = next_step
        return prev
