class TextEditor:
    def __init__(self):
        # pre: text before the cusor
        # post: text after the cursor
        self.pre = []
        self.post = []

    def addText(self, text: str) -> None:
        # Add text is simple: add to the end of pre
        self.pre.extend(text)

    def deleteText(self, k: int) -> int:
        # k might be larger than the length of the text, we
        # only delete maximum of chars_count chars
        chars_count = min(k, len(self.pre))

        del self.pre[-chars_count:]
        return chars_count

    def cursorLeft(self, k: int) -> str:
        """Move cursor left by moving chars from pre to post"""
        # Determine the maximum positions to move
        max_chars_count = min(k, len(self.pre))

        # Move
        self.post = self.pre[-max_chars_count:] + self.post
        del self.pre[-max_chars_count:]

        # Extract at most 10 chars to the left of the cursor
        max_chars_collected = min(10, len(self.pre))
        buf = self.pre[-max_chars_collected:]
        return "".join(buf)

    def cursorRight(self, k: int) -> str:
        """Move cursor right by moving chars from post to pre"""
        # Determine the maximum positions to move
        max_chars_count = min(k, len(self.post))

        # Move the chars
        self.pre.append(self.post[:max_chars_count])
        del self.post[:max_chars_count]

        # Extract at most 10 chars to the left of the cursor
        max_chars_collected = min(10, len(self.pre))
        buf = self.pre[-max_chars_collected:]
        return "".join(buf)
