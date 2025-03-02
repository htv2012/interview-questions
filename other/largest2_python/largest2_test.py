#!/usr/bin/env python3
"""
Given a list of integers, find 2 largest
1 3 4 5 6
"""
def largest2(ilist):
    if not ilist:
        return None, None

    smallest = largest = ilist[0]
    for element in ilist:
        if smallest > element:
            smallest = element
        if largest < element:
            largest = element

    if smallest == largest:
        return largest, None
    second_largest = smallest
    for element in ilist:
        if second_largest < element < largest:
            second_largest = element
    
    return largest, second_largest


def test_empty_list():
    assert largest2([]) == (None, None)


def test_happy_path():
    assert largest2([1, 2, 3, 4, 5]) == (5, 4)


def test_no_second():
    assert largest2([1, 1, 1]) == (1, None)


def test_duplicate_largest():
    assert largest2([1, 3, 3]) == (3, 1)


def test_first_element_is_largest():
    assert largest2([5, 3, 1]) == (5, 3)
