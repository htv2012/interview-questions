"""
https://leetcode.com/problems/first-bad-version/
"""

import json

import pytest

import solution


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
        pytest.param(
            int(2**31 - 1), int(2**31 - 2), int(2**31 - 2), id="edge, bad near the end"
        ),
        pytest.param(
            int(2**31 - 1), int(2**31 - 1), int(2**31 - 1), id="edge, bad at the end"
        ),
    ],
)
def test_solution(n, bad, expected, monkeypatch):
    monkeypatch.setattr(solution, "isBadVersion", lambda v: v >= bad)
    assert solution.first_bad_version(n) == expected


def test_not_found(monkeypatch):
    monkeypatch.setattr(solution, "isBadVersion", lambda v: v >= 500)
    with pytest.raises(ValueError):
        solution.first_bad_version(100)
