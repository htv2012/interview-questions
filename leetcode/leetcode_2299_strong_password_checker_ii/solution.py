import string

LOWER = set(string.ascii_lowercase)
UPPER = set(string.ascii_uppercase)
DIGITS = set(string.digits)
SPECIAL = set("!@#$%^&*()-+")


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        low = False
        up = False
        digit = False
        special = False
        last = ""

        if len(password) < 8:
            return False

        for i, ch in enumerate(password):
            if ch == last:
                return False
            if ch in LOWER:
                low = True
            if ch in UPPER:
                up = True
            if ch in DIGITS:
                digit = True
            if ch in SPECIAL:
                special = True
            if i >= 8 and low and up and digit and special:
                return True
            last = ch

        return low and up and digit and special
