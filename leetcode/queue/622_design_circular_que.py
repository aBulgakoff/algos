class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.previous = None


def link_nodes(left_node: Node, right_node: Node) -> None:
    left_node.next = right_node
    right_node.previous = left_node


def link_three_nodes(left_node: Node, mid_node: Node, right_node: Node) -> None:
    link_nodes(left_node, mid_node)
    link_nodes(mid_node, right_node)


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._head = Node(None)
        self._tail = Node(None)
        link_nodes(self._head, self._tail)
        self._size = 0
        self._capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            link_three_nodes(self._tail.previous, Node(value), self._tail)
            self._size += 1
            return True
        return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            link_nodes(self._head, self._head.next.next)
            self._size -= 1
            return True
        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self._head.next.value
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self._tail.previous.value
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return not self._size

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._capacity <= self._size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
