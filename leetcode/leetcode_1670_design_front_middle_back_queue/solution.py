NOT_FOUND = -1


class FrontMiddleBackQueue:
    def __init__(self):
        self.ar = []

    def pushFront(self, val: int) -> None:
        self.ar.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        if len(self.ar) < 2:
            self.pushFront(val)
            return

        mid_index = len(self.ar) // 2
        self.ar.insert(mid_index, val)

    def pushBack(self, val: int) -> None:
        self.ar.append(val)

    def popFront(self) -> int:
        if self.ar:
            return self.ar.pop(0)
        return NOT_FOUND

    def popMiddle(self) -> int:
        if not self.ar:
            return NOT_FOUND

        mid_index = (len(self.ar) - 1) // 2
        return self.ar.pop(mid_index)

    def popBack(self) -> int:
        if self.ar:
            return self.ar.pop()
        return NOT_FOUND

    # ======================================================================
    # Support
    # ======================================================================
    @property
    def front(self):
        if self.ar:
            return self.ar[0]
        return NOT_FOUND

    @property
    def mid(self):
        if not self.ar:
            return NOT_FOUND

        mid_index = (len(self.ar) - 1) // 2
        return self.ar[mid_index]

    @property
    def back(self):
        if self.ar:
            return self.ar[-1]
        return NOT_FOUND

    def __len__(self):
        return len(self.ar)

    def __repr__(self):
        return f"<Q len: {len(self)}, {self.ar!r}>"

    def __iter__(self):
        return iter(self.ar)


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
