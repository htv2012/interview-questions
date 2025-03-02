import pytest

from solution import Solution


@pytest.mark.parametrize(
    "order, s, expected",
    [
        pytest.param("cba", "abcd", "cbad", id="example 1"),
        pytest.param("bcafg", "abcd", "bcad", id="example 2"),
        pytest.param("cba", "banana", "baaann", id="custom 1"),
        pytest.param("skl", "alaska", "sklaaa", id="custom 2"),
    ],
)
def test_solution(order, s, expected):
    solution = Solution()
    assert solution.customSortString(order, s) == expected
