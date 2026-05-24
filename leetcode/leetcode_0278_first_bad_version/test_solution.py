"""
https://leetcode.com/problems/first-bad-version/
"""

import json

import pytest

from solution import first_bad_version


def create_api(bad: int):
    with open("/tmp/bad.json", "w") as stream:
        json.dump(bad, stream)


@pytest.mark.parametrize(
    ["n", "bad", "expected"],
    [
        pytest.param(5, 4, 4, id="Example 1"),
        pytest.param(1, 1, 1, id="Example 2"),
        pytest.param(1000, 25, 25, id="large list"),
    ],
)
def test_solution(n, bad, expected):
    create_api(bad)
    assert first_bad_version(n) == expected
