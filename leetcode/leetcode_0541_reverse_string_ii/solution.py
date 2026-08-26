class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a, b = 0, 2 * k
        buf = list(s)

        while a < len(buf):
            chunk = buf[a : a + k]
            buf[a : a + k] = chunk[::-1]
            a, b = b, min(b + (2 * k), len(buf))

        return "".join(buf)
