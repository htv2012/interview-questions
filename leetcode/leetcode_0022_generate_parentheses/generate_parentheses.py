class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        elif n == 1:
            return ["()"]

        out = set()
        for text in self.generateParenthesis(n - 1):
            out.add(f"(){text}")
            out.add(f"{text}()")
            out.add(f"({text})")
        return out
