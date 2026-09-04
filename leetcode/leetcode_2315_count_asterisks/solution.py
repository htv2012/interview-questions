class Solution:
    def countAsterisks(self, s: str) -> int:
        out = True  # outside of the bars
        count = 0

        for ch in s:
            if ch == "*" and out:
                count += 1
            if ch == "|":
                out = not out

        return count
