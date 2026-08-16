"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""

import pytest

from solution import Solution

GRAPH2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]


@pytest.mark.parametrize(
    "n, edges, source, destination, expected",
    [
        pytest.param(3, [[0, 1], [1, 2], [2, 0]], 0, 2, True, id="Example 1"),
        pytest.param(6, GRAPH2, 0, 5, False, id="Example 2"),
        pytest.param(6, GRAPH2, 0, 1, True, id="Example 2, 0-1"),
        pytest.param(6, GRAPH2, 2, 1, True, id="Example 2, 2-1"),
        pytest.param(6, GRAPH2, 2, 0, True, id="Example 2, 2-0"),
        pytest.param(6, GRAPH2, 3, 5, True, id="Example 2, 3-5"),
        pytest.param(0, [], 0, 1, False, id="empty graph"),
        pytest.param(1, [], 0, 0, True, id="source is destination"),
    ],
)
def test_solution(n, edges, source, destination, expected):
    sol = Solution()
    assert sol.validPath(n, edges, source, destination) is expected
