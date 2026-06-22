from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        for position, node in enumerate(self):
            if position == index:
                return node.val
        raise ValueError(f"Index out of range: {index}")

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
        raise NotImplementedError("addAtIndex")
        # if index == 0:
        #     self.addAtHead(val)
        #     return

        # current = self.head
        # previous = None
        # for _ in range(index):
        #     previous, current = current, current.next
        # node = Node(val, next=current)
        # previous.next = node

    def deleteAtIndex(self, index: int) -> None:
        raise NotImplementedError("deleteAtIndex")

    def __iter__(self):
        p = self.head
        while p:
            yield p
            p = p.next

    def __repr__(self):
        values = " ".join(str(p.val) for p, _ in zip(self, range(5)))
        return f"<{values}>"


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


li = MyLinkedList()
for i in range(4):
    li.addAtTail(i)
print(li)
