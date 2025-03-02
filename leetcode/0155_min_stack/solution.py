import collections

VAL = 0
MIN = 1


class MinStack:
    def __init__(self):
        self.data: collections.deque = collections.deque()

    def __repr__(self):
        return f"{self.__class__.__name__}(" f"data={self.data!r}" f")"

    def push(self, val: int) -> None:
        if self.data:
            min_so_far = min(self.data[-1][MIN], val)
        else:
            min_so_far = val
        self.data.append((val, min_so_far))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][VAL]

    def getMin(self) -> int:
        return self.data[-1][MIN]
