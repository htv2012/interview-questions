class Solution:
    def processStr(self, s: str, k: int) -> str:
        out = []
        for c in s:
            if c == "*":
                try:
                    out.pop()
                except IndexError:
                    pass
            elif c == "#":
                out.extend(out)
            elif c == "%":
                out.reverse()
            else:
                out.append(c)

        try:
            return out[k]
        except IndexError:
            return "."
