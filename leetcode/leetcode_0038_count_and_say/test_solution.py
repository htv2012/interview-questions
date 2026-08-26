import pytest

with open("n30.txt") as stream:
    n30 = stream.read().strip()


@pytest.mark.parametrize(
    ["n", "expected"],
    [
        pytest.param(4, "1211", id="Example 1"),
        pytest.param(1, "1", id="Example 2"),
        pytest.param(2, "11", id="n=2"),
        pytest.param(3, "21", id="n=3"),
        pytest.param(30, n30, id="n=30"),
    ],
)
def test_solution(fut, n, expected):
    assert fut(n) == expected
