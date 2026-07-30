NOT_FOUND = -1


class QueNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.val}]"


class FrontMiddleBackQueue:
    def __init__(self):
        self._front = None
        self._back = None
        self._len = 0

    def pushFront(self, val: int) -> None:
        node = QueNode(val)
        if len(self) == 0:
            self._front = self._back = node
        else:
            node.right = self._front
            self._front.left = node
            self._front = node
        self._len += 1

    def pushMiddle(self, val: int) -> None:
        pass

    def pushBack(self, val: int) -> None:
        node = QueNode(val)
        if len(self) == 0:
            self._back = self._front = node
        else:
            node.left = self._back
            self._back.right = node
            self._back = node
        self._len += 1

    def popFront(self) -> int:
        node = self._front
        if node is None:
            return NOT_FOUND

        self._len -= 1
        if self._len == 0:
            self._front = self._back = None
        else:
            self._front = node.right
            self._front.left = None

        return node.val

    def popMiddle(self) -> int:
        if self._len == 0:
            return NOT_FOUND
        elif self._len < 3:
            return self.popFront()

        node = self._get_mid()
        self._len -= 1
        left, right = node.left, node.right
        left.right = right
        right.left = left

        return node.val

    def popBack(self) -> int:
        node = self._back
        if node is None:
            return NOT_FOUND

        self._len -= 1
        if self._len == 0:
            self._front = self._back = None
        else:
            self._back = node.left
            self._back.right = None

        return node.val

    # ======================================================================
    # Support
    # ======================================================================
    @property
    def front(self):
        return self._front.val if self._front else NOT_FOUND

    @property
    def mid(self):
        node = self._get_mid()
        return NOT_FOUND if node is None else node.val

    @property
    def back(self):
        return self._back.val if self._back else NOT_FOUND

    def _get_mid(self):
        if self._len == 0:
            return None

        node = self._front
        for _ in range((self._len - 1) // 2):
            node = node.right
        return node

    def __len__(self):
        return self._len

    def __repr__(self):
        return f"<Q len: {self._len}, front: {self._front}, back: {self._back}>"

    def __iter__(self):
        node = self._front
        while node:
            yield node.val
            node = node.right


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
