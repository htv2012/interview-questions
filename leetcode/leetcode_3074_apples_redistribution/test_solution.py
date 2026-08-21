import pytest

from solution import Solution


@pytest.fixture
def minboxes():
    sol = Solution()
    return sol.minimumBoxes


@pytest.mark.parametrize(
    "apple, capacity, expected",
    [
        pytest.param([1, 3, 2], [4, 3, 1, 5, 2], 2, id="example 1"),
        pytest.param([5, 5, 5], [2, 4, 2, 7], 4, id="example 2"),
    ],
)
def test_solution(apple, capacity, expected, minboxes):
    assert minboxes(apple=apple, capacity=capacity) == expected
