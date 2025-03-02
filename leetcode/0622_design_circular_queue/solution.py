import pysnooper


class MyCircularQueue:
    def __init__(self, k: int):
        self.data = k * [None]
        self._capacity = k
        self.ip = 0  # Insertion point
        self.length = 0

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.length}/{self.capacity}"
            f", "
            f"ip={self.ip!r}"
            f", "
            f"data={self.data!r}"
            f")"
        )

    @property
    def capacity(self):
        return self._capacity

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[self.ip] = value
        self.length += 1
        self.ip = (self.ip + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # FIX: Should dequeue the front, not rear
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.ip - self.length) % self.capacity
        return self.data[index]

    @pysnooper.snoop("/tmp/snoop.txt")
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        index = (self.ip - 1) % self.capacity
        return self.data[index]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self._capacity == self.length
