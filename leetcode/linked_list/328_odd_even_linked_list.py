# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even_head = head.next
        odd_cursor, even_cursor = head, head.next

        while even_cursor and even_cursor.next:
            next_odd = even_cursor.next
            odd_cursor.next = next_odd
            odd_cursor = next_odd

            next_even = odd_cursor.next
            even_cursor.next = next_even
            even_cursor = next_even

        odd_cursor.next = even_head
        return head


class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head
        even_head = even = head.next
        node = even.next
        i = 3
        while node:
            if i % 2:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            i += 1
            node = node.next
        odd.next = even_head
        even.next = None
        return head
