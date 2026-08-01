class TextEditor:
    def __init__(self):
        self.pre = []
        self.post = []

    def addText(self, text: str) -> None:
        self.pre.extend(text)

    def deleteText(self, k: int) -> int:
        chars_count = min(k, len(self.pre))
        del self.pre[-chars_count:]
        return chars_count

    def cursorLeft(self, k: int) -> str:
        raise NotImplementedError("cursorLeft")

    def cursorRight(self, k: int) -> str:
        raise NotImplementedError("cursorRight")


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
