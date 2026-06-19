"""
https://leetcode.com/problems/search-a-2d-matrix
"""

import itertools

import pytest

from solution import Solution

TEST_MATRIX = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


@pytest.fixture
def fut():
    sol = Solution()
    return sol.searchMatrix


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["matrix"],
        kwargs["target"],
        kwargs["expected"],
        id=test_id,
    )


def generate_test_cases():
    for target in itertools.chain.from_iterable(TEST_MATRIX):
        yield tc(
            test_id=f"expect {target} found",
            matrix=TEST_MATRIX,
            target=target,
            expected=True,
        )
    for target in [0, 2, 4, 6, 8, 12, 15, 17, 21, 25, 32, 37, 90]:
        yield tc(
            test_id=f"expect {target} not found",
            matrix=TEST_MATRIX,
            target=target,
            expected=False,
        )

    large_matrix = [
        list(range(start * 100, (start * 100) + 100)) for start in range(100)
    ]
    for target in [0, 199, 9999]:
        yield tc(
            test_id=f"large matrix {target=}",
            matrix=large_matrix,
            target=target,
            expected=True,
        )
    for target in [-1, 10000]:
        yield tc(
            test_id=f"large matrix {target=}",
            matrix=large_matrix,
            target=target,
            expected=False,
        )


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        tc(
            test_id="Example 1",
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            target=3,
            expected=True,
        ),
        tc(
            test_id="Example 2",
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            target=13,
            expected=False,
        ),
        *generate_test_cases(),
    ],
)
def test_solution(fut, matrix, target, expected):
    assert fut(matrix, target) is expected
