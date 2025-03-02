#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("/home/", "/home", id="example 1"),
        pytest.param("/../", "/", id="example 2"),
        pytest.param("/home//foo/", "/home/foo", id="example 3"),
        pytest.param("/a/../../b/../c//.//", "/c", id="wrong 1"),
        pytest.param("/usr/./lib/.././bin", "/usr/bin", id="custom 1"),
        pytest.param("/foo/bar/../..", "/", id="custom 2"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
