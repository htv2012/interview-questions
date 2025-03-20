import collections

class DB:
    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.values = collections.defaultdict(set)

    def add(self, value: int):
        old_count = self.freq[value]
        self.freq[value] += 1

        if old_count != 0:
            self.values[old_count].discard(value)
        self.values[old_count + 1].add(value)

    def query_frequency(self, frequency):
        return self.values[frequency] != set()
        
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"freq={self.freq!r}"
            f", "
            f"values={self.values!r}"
            f")"
        )
