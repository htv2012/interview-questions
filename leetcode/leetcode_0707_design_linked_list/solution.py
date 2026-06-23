from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None

    def __repr__(self):
        return f"({self.val})"


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        for position, node in enumerate(self):
            if position == index:
                return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, next=self.head)
        self.head = node
        if self.tail is None:
            # case: add head when list is empty
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

        if self.head is None:
            self.head = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        for position, previous in enumerate(self):
            if position == index - 1:
                node = Node(val, next=previous.next)
                previous.next = node
                return

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            if self.tail is self.head:
                # case: single node
                self.tail = None
            to_be_deleted_node = self.head
            self.head = to_be_deleted_node.next

        for position, previous in enumerate(self):
            if position == index - 1:
                to_be_deleted_node = previous.next
                previous.next = to_be_deleted_node.next
                return

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        values = " → ".join(str(node) for node in self)
        if len(values) > 40:
            values = f"{values[:36]} ..."
        return f"<{values}>"


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
