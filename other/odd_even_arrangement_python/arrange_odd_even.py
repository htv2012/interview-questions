#!/usr/bin/env python
"""
Given a list of integers containing equal number of odd and even
numbers rearrange them in such a way that odd number is at odd
zero-based index.
"""


def isodd(number):
    """ Returns 0 if even, 1 if odd """
    return number % 2


def arrange_odd_even(seq):
    """
    Given a list of integers containing equal number of odd and
    even numbers rearrange them in such a way that odd number is
    at odd zero-based index.
    """
    length = len(seq)
    odd_index = 1
    even_index = 0
    print seq
    while True:
        while odd_index < length and isodd(seq[odd_index]) == 1:
            odd_index += 2

        while even_index < length and isodd(seq[even_index]) == 0:
            even_index += 2

        if odd_index >= length or even_index >= length:
            break

        seq[odd_index], seq[even_index] = seq[even_index], seq[odd_index]
