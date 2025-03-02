#!/usr/bin/env python3
"""
Given a list and a target, find the sum of elements which equates to the target

For example:

* list = [1, 2, 3, 4, 5]
* target = 6

Function should return [[1, 2, 3], [1, 5], [2, 4]]
"""


def find_sums(li, target):
    li_copy = li[:]
    results = []
    while li_copy:
        element = li_copy.pop()
        if element == target:
            results.append([element])
            continue
        elif element > target:
            continue

        for result in find_sums(li_copy, target - element):
            result.append(element)
            if result not in results:
                results.append(result)
    return results


def test1():
    li = [1, 2]
    target = 2
    actual = list(find_sums(li, target))
    assert actual == [[2]]


def test2():
    assert find_sums([1, 2], 3) == [[1, 2]]


def test3():
    actual = find_sums([1, 2, 3, 4, 5, 6, 7, 8], 6)
    assert [1, 2, 3] in actual
    assert [1, 5] in actual
    assert [2, 4] in actual
    assert [6] in actual
    assert len(actual) == 4





