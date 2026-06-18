"""
https://leetcode.com/problems/valid-number
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.isNumber


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                s="0",
                expected=True,
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                s="e",
                expected=False,
            ),
            id="Example 2",
        ),
        pytest.param(
            types.SimpleNamespace(
                s=".",
                expected=False,
            ),
            id="Example 3",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.s) is test_case.expected


@pytest.mark.parametrize(
    "s",
    [
        "2",
        "0089",
        "-0.1",
        "+3.14",
        "4.",
        "-.9",
        "2e10",
        "-90E3",
        "3e+7",
        "+6e-1",
        "53.5e93",
        "-123.456e789",
    ],
)
def test_valid(fut, s):
    assert fut(s)


@pytest.mark.parametrize(
    "s",
    [
        "",
        " ",
        "foo",
        ".",
        "abc",
        "1a",
        "1e",
        "e3",
        "99e2.5",
        "--6",
        "-+3",
        "95a54e53",
        "-",
        "+",
        "-.E3",
        "12e",
    ],
)
def test_not_valid(fut, s):
    assert not fut(s)
