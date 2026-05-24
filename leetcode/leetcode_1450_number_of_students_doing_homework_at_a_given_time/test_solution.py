"""
https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/
"""

import pytest

from solution import busy_student


@pytest.mark.parametrize(
    ["start_time", "end_time", "query_time", "expected"],
    [
        pytest.param([1, 2, 3], [3, 2, 7], 4, 1, id="Example 1"),
        pytest.param([4], [4], 4, 1, id="Example 2"),
        pytest.param([1, 1, 1, 0, 7], [2, 3, 5, 1, 9], 1, 4, id="happy path 1"),
        pytest.param([], [], 1, 0, id="empty lists"),
        pytest.param([1], [2], 3, 0, id="single student"),
    ],
)
def test_solution(start_time, end_time, query_time, expected):
    assert busy_student(start_time, end_time, query_time) == expected
