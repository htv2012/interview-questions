import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.maximumHappinessSum


@pytest.mark.parametrize(
    "happiness, k, expected",
    [
        pytest.param([1, 2, 3], 2, 4, id="example 1"),
        pytest.param([1, 1, 1, 1], 2, 1, id="example 2"),
        pytest.param([12, 1, 42], 3, 53, id="edge case 1"),
    ],
)
def test_solution(happiness, k, expected, fut):
    assert fut(happiness=happiness, k=k) == expected
