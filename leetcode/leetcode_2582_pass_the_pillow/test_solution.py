"""
https://leetcode.com/problems/pass-the-pillow/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "n, time, expected",
    [
        pytest.param(4, 5, 2, id="Example 1"),
        pytest.param(3, 2, 3, id="Example 2"),
        pytest.param(1, 3, 1, id="n=1, t=3"),
        pytest.param(2, 5, 2, id="n=2, t=5"),
        pytest.param(2, 4, 1, id="n=2, t=4"),
        pytest.param(5, 1, 2, id="n=5, t=1"),
        pytest.param(5, 2, 3, id="n=5, t=2"),
        pytest.param(5, 4, 5),
        pytest.param(5, 5, 4),
        pytest.param(5, 8, 1),
    ],
)
def test_solution(n, time, expected):
    sol = Solution()
    assert sol.passThePillow(n, time) == expected
