import bisect


class StockPrice:
    def __init__(self):
        self.latest = 0  # latest time stamp
        self.price = {}  # stamp: price
        self.sorted = []  # prices sorted low to high

    def update(self, timestamp: int, price: int) -> None:
        if (old_price := self.price.get(timestamp, 0)) > 0:
            i = bisect.bisect_left(self.sorted, old_price)
            del self.sorted[i]

        self.price[timestamp] = price
        bisect.insort(self.sorted, price)
        self.latest = max(self.latest, timestamp)

    def current(self) -> int:
        return self.price[self.latest]

    def maximum(self) -> int:
        return self.sorted[-1]

    def minimum(self) -> int:
        return self.sorted[0]
