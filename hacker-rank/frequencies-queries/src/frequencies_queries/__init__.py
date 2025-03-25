class DB:
    def __init__(self):
        self.freq = {}

    def add(self, value: int):
        self.freq.setdefault(value, 0)
        self.freq[value] += 1

    def remove(self, value):
        current_count = self.freq.get(value)
        if current_count is None:
            return
        if current_count == 1:
            del self.freq[value]
        else:
            self.freq[value] -= 1

    def query_frequency(self, frequency):
        return frequency in self.freq.values()

    def __repr__(self):
        return f"{self.__class__.__name__}(freq={self.freq!r})"
