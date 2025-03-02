class MyCircularDeque:
    def __init__(self, k: int):
        self._capacity = k
        self.data = k * [None]
        self.clear()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.length}/{self.capacity}"
            f", "
            f"{self.data!r}"
            f", "
            f"f={self.front!r}"
            f", "
            f"r={self.rear!r}"
            f")"
        )

    @property
    def capacity(self):
        return self._capacity

    def advance(self, index: int, delta: int) -> int:
        return (index + delta) % self.capacity

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 1
            self.data[self.front] = value
            self.length = 1
        else:
            self.front = self.advance(self.front, -1)
            self.data[self.front] = value
            self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = 0
                self.rear = 0
            self.data[self.rear] = value
            self.rear = self.advance(self.rear, 1)
            self.length += 1
            return True

    def clear(self):
        self.length = 0
        self.front = -1
        self.rear = 0

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.length -= 1
        if self.isEmpty():
            self.clear()
        else:
            self.front = self.advance(self.front, 1)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.length -= 1
        if self.isEmpty():
            self.clear()
        else:
            self.rear = self.advance(self.rear, -1)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        index = self.advance(self.rear, -1)
        return self.data[index]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
