

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        buf = []
        for chars in zip(*strs):
            if any(ch != chars[0] for ch in chars):
                break
            buf.append(chars[0])

        return "".join(buf)
