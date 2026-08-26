class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        out = [word for word in words if any(set(word.lower()) <= row for row in rows)]
        return out
