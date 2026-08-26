# Reverse vowels in a string
VOWELS = set("aeiouAEIOU")


class Solution:
    def reverseVowels(self, s: str) -> str:
        buf = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if buf[left] not in VOWELS:
                left += 1
            elif buf[right] not in VOWELS:
                right -= 1
            else:
                buf[left], buf[right] = buf[right], buf[left]
                left += 1
                right -= 1
        return "".join(buf)
