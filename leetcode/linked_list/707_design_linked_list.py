class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


def link_two_nodes(left_node: ListNode, right_node: ListNode) -> None:
    left_node.next = right_node
    right_node.previous = left_node


def link_three_nodes(left_node: ListNode,
                     mid_node: ListNode,
                     right_node: ListNode) -> None:
    link_two_nodes(left_node, mid_node)
    link_two_nodes(mid_node, right_node)


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sentinel_head = ListNode(None)
        self.sentinel_tail = ListNode(None)
        link_two_nodes(self.sentinel_head, self.sentinel_tail)
        self.size = 0

    def _get_node(self, index: int, including_sentinels=True) -> ListNode:
        if including_sentinels:
            if index < 0 or index > self.size:
                raise IndexError('%i index is incorrect' % index)
        else:
            if index < 0 or index + 1 > self.size:
                raise IndexError('%i index is incorrect' % index)

        if index < self.size / 2:
            coursor = self.sentinel_head.next
            coursor_index = 0
            while coursor_index < index:
                coursor = coursor.next
                coursor_index += 1
        else:
            coursor = self.sentinel_tail
            coursor_index = self.size
            while coursor_index > index:
                coursor = coursor.previous
                coursor_index -= 1
        return coursor

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        try:
            node = self._get_node(index, including_sentinels=False)
        except IndexError:
            return -1
        return node.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        try:
            next_node = self._get_node(index)
        except IndexError:
            return
        previous_node = next_node.previous
        new_node = ListNode(val)
        link_three_nodes(previous_node, new_node, next_node)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        try:
            node = self._get_node(index, including_sentinels=False)
        except IndexError:
            return
        link_two_nodes(node.previous, node.next)
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
