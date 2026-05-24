"""
https://leetcode.com/problems/first-bad-version/
"""

import json

import pytest

import solution
from solution import first_bad_version


def create_api(bad: int):
    with open("/tmp/bad.json", "w") as stream:
        json.dump(bad, stream)


@pytest.mark.parametrize(
    ["n", "bad", "expected"],
    [
        pytest.param(5, 4, 4, id="Example 1"),
        pytest.param(1, 1, 1, id="Example 2"),
        pytest.param(1000, 25, 25, id="large list, bad early"),
        pytest.param(1000, 998, 998, id="large list, bad late"),
        pytest.param(1, 1, 1, id="single version"),
        pytest.param(2, 1, 1, id="2 versions, first one bad"),
        pytest.param(2, 2, 2, id="2 versions, last one bad"),
        pytest.param(10, 11, -1, id="no bad version found"),
    ],
)
def test_solution(n, bad, expected, monkeypatch):
    monkeypatch.setattr(solution, "isBadVersion", lambda v: v >= bad)
    assert first_bad_version(n) == expected
