# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel_head = cursor = ListNode(None)
        l1_cursor, l2_cursor = l1, l2
        carry = 0

        while l1_cursor or l2_cursor or carry:
            l1_value = l1_cursor.val if l1_cursor else 0
            l2_value = l2_cursor.val if l2_cursor else 0
            carry, summed = divmod(carry + l1_value + l2_value, 10)

            cursor.next = ListNode(summed)
            cursor = cursor.next

            l1_cursor = l1_cursor.next if l1_cursor else l1_cursor
            l2_cursor = l2_cursor.next if l2_cursor else l2_cursor

        return sentinel_head.next
