import pathlib

import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("aaba*", "aab", id="example 1"),
        pytest.param("abc", "abc", id="example 2"),
        pytest.param("ed", "ed", id="wrong 1"),
        pytest.param("r" * 50000 + "*" * 49999, "r", id="long string"),
        pytest.param(pathlib.Path("case4.txt").read_text(), "", id="very long string"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
