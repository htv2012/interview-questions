class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        num = abs(num)
        buf = []

        while num != 0:
            num, rem = divmod(num, 7)
            buf.append(str(rem))
        if neg:
            buf.append("-")

        buf.reverse()
        return "".join(buf)
        buf = []
