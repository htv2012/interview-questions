import collections


class DB:
    def __init__(self):
        self.freq = collections.defaultdict(int)
        # self.values = collections.defaultdict(set)

    def add(self, value: int):
        self.freq[value] += 1
        # old_count = self.freq[value]
        # self.freq[value] += 1

        # if old_count != 0:
        #     self.values[old_count].discard(value)
        # self.values[old_count + 1].add(value)

    def remove(self, value):
        if self.freq[value] == 0:
            return
        self.freq[value] -= 1

    def query_frequency(self, frequency):
        return frequency in self.freq.values()
        # return self.values[frequency] != set()

    def __repr__(self):
        return f"{self.__class__.__name__}(freq={self.freq!r}, values={self.values!r})"
