import random


class RandomizedSet:
    def __init__(self):
        self.data = {}

    def insert(self, val: int) -> bool:
        success = val not in self.data
        self.data[val] = True
        return success

    def remove(self, val: int) -> bool:
        try:
            del self.data[val]
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        value = random.choice(self.data)
        return value
