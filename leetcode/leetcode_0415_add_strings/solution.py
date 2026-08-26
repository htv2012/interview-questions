import itertools


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        stack = []
        digit = {str(d): d for d in range(10)}

        for a, b in itertools.zip_longest(
            reversed(num1), reversed(num2), fillvalue="0"
        ):
            carry, total = divmod(digit[a] + digit[b] + carry, 10)
            stack.append(total)
        if carry > 0:
            stack.append(carry)

        stack.reverse()
        answer = "".join(str(d) for d in stack)
        return answer
