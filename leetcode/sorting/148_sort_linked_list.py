[-84, 142, 41, -17, -71, 170, 186, 183, -21, -76, 76, 10, 29, 81, 112, -39, -6, -43, 58, 41, 111, 33, 69, 97, -38, 82,
 -44, -7, 99, 135, 42, 150, 149, -21, -30, 164, 153, 92, 180, -61, 99, -81, 147, 109, 34, 98, 14, 178, 105, 5, 43, 46,
 40, -37, 23, 16, 123, -53, 34, 192, -73, 94, 39, 96, 115, 88, -31, -96, 106, 131, 64, 189, -91, -34, -56, -22, 105,
 104, 22, -31, -43, 90, 96, 65, -85, 184, 85, 90, 118, 152, -31, 161, 22, 104, -85, 160, 120, -31, 144, 115]

[-96, -91, -85, -85, -84, -81, -76, -73, -71, -61, -56, -53, -44, -43, -43, -39, -38, -37, -34, -31, -31, -31, -31, -30,
 -22, -21, -21, -17, -7, -6, 5, 10, 14, 16, 22, 22, 23, 29, 33, 34, 34, 39, 40, 41, 41, 42, 43, 46, 58, 64, 65, 69, 76,
 81, 82, 85, 88, 90, 90, 92, 94, 96, 96, 97, 98, 99, 99, 104, 104, 105, 105, 106, 109, 111, 112, 115, 115, 118, 120,
 123, 131, 135, 142, 144, 147, 149, 150, 152, 153, 160, 161, 164, 170, 178, 180, 183, 184, 186, 189, 192]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def get_size(node):
            counter = 0
            while node:
                counter += 1
                node = node.next
            return counter

        def split(node, position):
            index = 1
            while index < position and node:
                node = node.next
                index += 1

            if not node:
                return node

            temp_node, node.next = node.next, None
            return temp_node

        def merge(left, right, node):
            cursor = node
            while left and right:
                if left.val < right.val:
                    cursor.next, left = left, left.next
                else:
                    cursor.next, right = right, right.next
                cursor = cursor.next

            cursor.next = left if left else right
            while cursor.next:
                cursor = cursor.next
            return cursor

        length = get_size(head)
        dummy = ListNode(0)
        dummy.next = head
        left, right, tail = None, None, None

        step = 1
        while step < length:
            head = dummy.next
            tail = dummy
            while head:
                left = head
                right = split(left, step)
                head = split(right, step)
                tail = merge(left, right, tail)
            step <<= 1

        return dummy.next
