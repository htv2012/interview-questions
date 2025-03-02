class Solution:
    def removeStars(self, s: str) -> str:
        buffer = []
        for c in s:
            if c == "*":
                buffer.pop()
            else:
                buffer.append(c)
        return "".join(buffer)
