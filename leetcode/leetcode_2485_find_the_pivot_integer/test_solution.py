import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.pivotInteger


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(8, 6, id="example 1"),
        pytest.param(1, 1, id="example 2"),
        pytest.param(4, -1, id="example 2"),
        pytest.param(49, 35, id="n=49, x=35"),
        pytest.param(288, 204, id="n=288, x=204"),
    ]
    + [
        pytest.param(n, -1, id=f"{n=} x=-1")
        for n in range(2, 1001)
        if n not in {8, 1, 4, 49, 288}
    ],
)
def test_solution(n, expected, fut):
    assert fut(n) == expected
