class Solution:
    def clearStars(self, s: str) -> str:
        out = []
        for c in s:
            if c == "*":
                smallest = min(out)
                index = len(out) - 1
                while out[index] != smallest:
                    index -= 1
                out.pop(index)
            else:
                out.append(c)
        return "".join(out)


if __name__ == "__main__":
    f = Solution().clearStars()
