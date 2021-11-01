# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        i = 0

        last_before_merge = None
        while list1 or list2:
            if i + 1 == a:
                last_before_merge = list1
                list1 = list1.next
                last_before_merge.next = list2
                while list2.next:
                    list2 = list2.next
            if i + 1 == b:
                list2.next = list1.next
                list1.next = None
                break
            list1 = list1.next
            i += 1

        return head
