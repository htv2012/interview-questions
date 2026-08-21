import logging
import math
import shlex

logger = logging.getLogger("fraction")


class Fraction:
    def __init__(self, num: int, dem: int):
        self.num = num
        self.dem = int(dem)

    def __str__(self):
        return f"{self.num}/{self.dem}"

    def __repr__(self) -> str:
        return f"F({self})"

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            return NotImplemented

        this = Fraction(self.num, self.dem)
        this.reduce()
        that = Fraction(other.num, other.dem)
        that.reduce()
        return this.num == that.num and this.dem == that.dem

    def reduce(self):
        gcd = math.gcd(self.num, self.dem)
        self.num //= gcd
        self.dem //= gcd

    def __add__(self, other) -> "Fraction":
        logger.debug(f"adding {self=} to {other=}")
        if not isinstance(other, Fraction):
            logger.debug(
                f"cannot add to {other}({other.__class__.__name__}), return not implemented."
            )
            return NotImplemented

        lcm = math.lcm(self.dem, other.dem)

        self_num = self.num * lcm // self.dem
        other_num = other.num * lcm // other.dem

        result = Fraction(self_num + other_num, lcm)
        logger.debug(f"before reduce, {result = }")
        result.reduce()
        logger.debug(f"after reduce, {result = }")

        return result

    def __radd__(self, other) -> "Fraction":
        logger.debug(f"reverse add {self=} to {other=}")
        if isinstance(other, int):
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            return self + other

        return NotImplemented


def parse_expression(expr: str):  # -> list[Fraction]:
    tokens = shlex.shlex(expr)
    stack = []

    for token in tokens:
        if token.isdigit() and len(stack) >= 2 and stack[-1] == "/":
            stack.pop()  # Remove the slash, '/'
            num = stack.pop()

            if stack and (stack[-1] == "+" or stack[-1] == "-"):
                sign = stack.pop()
                num = f"{sign}{num}"

            stack.append(Fraction(int(num), int(token)))
        else:
            stack.append(token)

    return stack


class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = parse_expression(expression)
        total = sum(stack)
        return str(total)
