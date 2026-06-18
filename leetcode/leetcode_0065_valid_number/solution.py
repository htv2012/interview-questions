import logging

logger = logging.getLogger()

TOKEN_SIGN = "sign"
TOKEN_DOT = "dot"
TOKEN_DIGIT = "digit"
TOKEN_EXPONENT = "exponent"

STATE_START = "start"
STATE_PRE_DOT_DIGITS = "pre-dots digits"
STATE_POST_DOT_DIGITS = "post-dots digits"
STATE_POST_EXPONENT_DIGITS = "post exponents"
STATE_DOT = "dot"
STATE_DOT_WITHOUT_DIGITS = "dot without digit"
STATE_EXPONENT = "exponent"
STATE_POST_EXPONENT_SIGN = "post exponent sign"


def tokenize(ch: str):
    if ch == "-" or ch == "+":
        return TOKEN_SIGN
    elif ch == ".":
        return TOKEN_DOT
    elif "0" <= ch <= "9":
        return TOKEN_DIGIT
    elif ch == "e" or ch == "E":
        return TOKEN_EXPONENT
    raise ValueError(f"Unknown char: {ch!r}")


state_machine = {
    STATE_START: {
        TOKEN_SIGN: STATE_PRE_DOT_DIGITS,
        TOKEN_DOT: STATE_DOT_WITHOUT_DIGITS,
        TOKEN_DIGIT: STATE_PRE_DOT_DIGITS,
    },
    STATE_PRE_DOT_DIGITS: {
        TOKEN_DOT: STATE_DOT,
        TOKEN_DIGIT: STATE_PRE_DOT_DIGITS,
        TOKEN_EXPONENT: STATE_EXPONENT,
    },
    STATE_DOT: {
        TOKEN_DIGIT: STATE_POST_DOT_DIGITS,
        TOKEN_EXPONENT: STATE_EXPONENT,
    },
    STATE_DOT_WITHOUT_DIGITS: {
        TOKEN_DIGIT: STATE_POST_DOT_DIGITS,
    },
    STATE_POST_DOT_DIGITS: {
        TOKEN_DIGIT: STATE_POST_DOT_DIGITS,
        TOKEN_EXPONENT: STATE_EXPONENT,
    },
    STATE_EXPONENT: {
        TOKEN_DIGIT: STATE_POST_EXPONENT_DIGITS,
        TOKEN_SIGN: STATE_POST_EXPONENT_SIGN,
    },
    STATE_POST_EXPONENT_SIGN: {
        TOKEN_DIGIT: STATE_POST_EXPONENT_DIGITS,
    },
    STATE_POST_EXPONENT_DIGITS: {
        TOKEN_DIGIT: STATE_POST_EXPONENT_DIGITS,
    },
}

terminals = set(
    [
        STATE_PRE_DOT_DIGITS,
        STATE_POST_DOT_DIGITS,
        STATE_POST_EXPONENT_DIGITS,
        STATE_DOT,
    ]
)


class Solution:
    def isNumber(self, s: str) -> bool:
        # Edge case: missing digit either before or after 'e'
        digits = set("0123456789")
        if not all(digits.intersection(group) for group in s.lower().split("e")):
            return False

        state = STATE_START
        try:
            for ch in s:
                token = tokenize(ch)
                prev_state, state = state, state_machine[state][token]
                logger.debug(f"[{prev_state}] + {ch!r}({token}) -> [{state}]")
            return state in terminals
        except ValueError as err:
            logger.error(f"[{state}] + {ch!r} -> ERROR: {err}")
            return False
        except KeyError as err:
            logger.error(f"[{state}] + {ch!r} -> Invalid token for this state: {err}")
            return False
