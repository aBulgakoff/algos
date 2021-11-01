from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(1, k):
            fast = fast.next
        swap = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        swap.val, slow.val = slow.val, swap.val

        return head
