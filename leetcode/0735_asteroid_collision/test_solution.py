import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([5, 10, -5], [5, 10], id="example 1"),
        pytest.param([8, -8], [], id="example 2"),
        pytest.param([10, 2, -5], [10], id="example 3"),
        pytest.param([-2, -1, 1, 2], [-2, -1, 1, 2], id="wrong 1"),
        pytest.param([-2, -2, 1, -2], [-2, -2, -2], id="wrong 2"),
        pytest.param([1, 2, 3, 4, 5, -6], [-6], id="kill all the left elements"),
        pytest.param([1, 2, 3, -2, -1], [1, 2, 3], id="kill all the right elements"),
        pytest.param([], [], id="empty"),
        pytest.param([1], [1], id="single element"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
