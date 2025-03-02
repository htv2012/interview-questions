#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20, id="example 1"),
        pytest.param(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            32,
            id="example 2",
        ),
        pytest.param("a", 0, id="example 3"),
        pytest.param("a.txt", 5, id="wrong 1"),
        pytest.param("dir\n        file.txt", 16, id="wrong 2"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
