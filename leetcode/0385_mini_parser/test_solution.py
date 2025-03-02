#!/usr/bin/env python3
import pytest

from nested_integer import NestedInteger


def convert_to_list(nested_integer: NestedInteger):
    if nested_integer.isInteger():
        return nested_integer.getInteger()
    return [convert_to_list(element) for element in nested_integer.getList()]


@pytest.mark.parametrize(
    "in_data, expected",
    [
        pytest.param("324", 324, id="example 1"),
        pytest.param("[123,[456,[789]]]", [123, [456, [789]]], id="example 2"),
        pytest.param("-5", -5, id="negative int"),
        pytest.param("[-1,[-2,-3]]", [-1, [-2, -3]], id="negative ints in lists"),
        pytest.param("[[123],[456]]", [[123], [456]], id="comma between lists"),
        pytest.param("[]", [], id="empty list"),
    ],
)
def test_solution(fut, in_data, expected):
    actual = fut(in_data)
    assert convert_to_list(actual) == expected
