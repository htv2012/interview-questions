"""
https://leetcode.com/problems/process-string-with-special-operations-ii/description/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.processStr


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                s="a#b%*",
                k=1,
                expected="a",
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                s="cd%#*#",
                k=3,
                expected="d",
            ),
            id="Example 2",
        ),
        pytest.param(
            types.SimpleNamespace(
                s="z*#",
                k=0,
                expected=".",
            ),
            id="Example 3",
        ),
        pytest.param(
            types.SimpleNamespace(
                s="%#bz%xum##i##vzo#pwc*#dkwbh####%uf%s*%cgppqhqa%h#l##o%ij%%cz%iga##e###u%#e####jfwx##%%*x%m*%#",
                k=6523,
                expected="z",
            ),
            id="Memory Limit Exceeded",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.s, test_case.k) == test_case.expected
