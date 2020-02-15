# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        slow_cursor = head
        fast_cursor = head

        # find mid: when fast reaches end slow is at mid
        while fast_cursor.next and fast_cursor.next.next:
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next.next

        # reverse 2nd part of lsit
        previous_node = None
        current_node = slow_cursor.next
        while current_node:
            next_node = current_node.next  # save next node
            current_node.next = previous_node  # link previous nodes
            previous_node = current_node  # save current node
            current_node = next_node  # move to next

        # connect first part to mid with reversed starting on last element
        slow_cursor.next = previous_node

        # palindrome check
        # iterate with two pointers from mid till last and from beginning till mid comparting values
        main_cursor = head
        reversed_cursor = previous_node
        while reversed_cursor:
            if main_cursor.val != reversed_cursor.val:
                return False
            main_cursor = main_cursor.next
            reversed_cursor = reversed_cursor.next
        return True

