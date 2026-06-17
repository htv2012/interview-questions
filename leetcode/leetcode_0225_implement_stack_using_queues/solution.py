class MyStack:
    def __init__(self):
        self.data = [None] * 100
        self.tos = -1  # top of stack

    def push(self, x: int) -> None:
        self.tos += 1
        self.data[self.tos] = x

    def pop(self) -> int:
        value = self.data[self.tos]
        self.tos -= 1
        return value

    def top(self) -> int:
        return self.data[self.tos]

    def empty(self) -> bool:
        return self.tos == -1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
