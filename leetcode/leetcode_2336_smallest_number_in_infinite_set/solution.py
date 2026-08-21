class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1
        self.out = set()

    def popSmallest(self) -> int:
        result = self.smallest
        self.out.add(result)
        while self.smallest in self.out:
            self.smallest += 1
        return result

    def addBack(self, num: int) -> None:
        self.out.discard(num)
        self.smallest = min(self.smallest, num)
