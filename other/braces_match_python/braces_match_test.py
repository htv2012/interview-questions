"""
Given a string s containing characters '(', ')', '{', '}', '[' ,
']', etc.  determine if the input string is valid.  An input string
is valid if:
    a. Open brackets must be closed by the same type of brackets.
    b. Open brackets must be closed in the correct order.
"""
import pytest


def braces_match(text: str) -> bool:
    stack = []
    for c in text or []:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            try:
                open_brace = stack.pop()
                if not ((open_brace == "(" and c == ")") or (open_brace == "[" and c == "]") or (open_brace == "{" and c == "}")):
                    return False
            except IndexError:
                return False
    
    return not stack


POSITIVE_CASES = [
    None,
    "",
    "hello",
    "(hello)",
    "{hello}",
    "[hello]",
    "[one {two (three)}]",
    "[][][]",
    "(one(two(three)))",
    "[[[]]]",
]

NEGATIVE_CASES = [
    "]",
    "[",
    "(",
    ")",
    "{",
    "}",
    "hello]",
    "hello)",
    "hello}",
    "(foo {bar)}",
    "[)",
]


@pytest.mark.parametrize("value", POSITIVE_CASES)
def test_positive(value):
    assert braces_match(value) is True


@pytest.mark.parametrize("value", NEGATIVE_CASES)
def test_negative(value):
    assert braces_match(value) is False
