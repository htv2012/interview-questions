class MapSum:
    def __init__(self):
        self.ms = {}

    def insert(self, key: str, val: int) -> None:
        self.ms[key] = val

    def sum(self, prefix: str) -> int:
        return sum(value for key, value in self.ms.items() if key.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
