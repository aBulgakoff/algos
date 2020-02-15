# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_A = set()
        cursor_A = headA
        cursor_B = headB
        while cursor_A:
            nodes_A.add(cursor_A)
            cursor_A = cursor_A.next
        while cursor_B:
            if cursor_B in nodes_A:
                return cursor_B
            cursor_B = cursor_B.next
        return None
