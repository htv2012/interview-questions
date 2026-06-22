from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    val: int
    next: Optional[Any] = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        p = self.head
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, next=self.head)
        if self.tail is None:
            self.tail = node
        if self.head:
            self.head.next = node
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        previous = None
        for _ in range(index):
            previous, current = current, current.next
        node = Node(val, next=current)
        previous.next = node

    def deleteAtIndex(self, index: int) -> None:
        raise NotImplementedError("deleteAtIndex")

    def __iter__(self):
        p = self.head
        while p:
            yield p
            p = p.next

    def __repr__(self):
        return f"<{','.join(str(p.val) for p in self)}>"


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


li = MyLinkedList()
li.addAtHead(1)
print(li)
li.addAtIndex(0, -9)
print(li)