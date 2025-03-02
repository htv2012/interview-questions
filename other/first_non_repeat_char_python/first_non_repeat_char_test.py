#!/usr/bin/env python3
"""
Given a string, write a function to return the first non-repeat
char in that string
"""


def first_non_repeat_char(buffer):
    """
    Given a string `buffer`, return the first non-repeat char in
    that string. Return "" if not found.
    """
    count = {}
    for c in buffer:
        count.setdefault(c, 0)
        count[c] += 1
    
    for c in buffer:
        if count[c] == 1:
            return c

    return ""    


def test_happy_path():
    assert first_non_repeat_char("abcaacccd") == "b"


def test_last_char_returned():
    assert first_non_repeat_char("abcabcd") == "d"


def test_none_found():
    assert first_non_repeat_char("aaabbbccc") == ""


def test_empty_string():
    assert first_non_repeat_char("") == ""
