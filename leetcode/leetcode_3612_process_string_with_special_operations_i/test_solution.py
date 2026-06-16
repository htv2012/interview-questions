"""
https://leetcode.com/problems/process-string-with-special-operations-i/
"""

import types

import pytest


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                s='a#b%*',
                expected='ba',
            ),
            id='Example 1',
        ),
        pytest.param(
            types.SimpleNamespace(
                s='z*#',
                expected='',
            ),
            id='Example 2',
        ),
    ]
)
def test_solution(fut, test_case):
    pass
