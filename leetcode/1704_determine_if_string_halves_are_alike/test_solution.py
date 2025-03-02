#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param("book", True, id="example 1"),
        pytest.param("textbook", False, id="example 2"),
        pytest.param("AbCdEfGh", True, id="wrong 1"),
        pytest.param("abcdttta", True, id="mine1"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) is expected
