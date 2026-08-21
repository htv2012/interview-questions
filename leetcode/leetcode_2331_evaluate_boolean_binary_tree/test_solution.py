import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([2, 1, 3, None, None, 0, 1], True, id="example 1"),
        pytest.param([0], False, id="example 2"),
        pytest.param(
            [
                3,
                3,
                2,
                0,
                0,
                3,
                2,
                None,
                None,
                None,
                None,
                1,
                3,
                1,
                1,
                None,
                None,
                2,
                1,
                None,
                None,
                None,
                None,
                1,
                1,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            False,
            id="wrong 1",
        ),
        pytest.param([3, 0, 0], False, id="wrong 1, top left"),
        pytest.param([3, 2, 1, 1, 1], True, id="wrong 1, bottom most"),
        pytest.param(
            [3, 1, 3, None, None, 2, 1, 1, 1], True, id="wrong 1, bottom  rightmost"
        ),
        pytest.param([2, 1, 1], True, id="wrong 1, right most"),
        pytest.param(
            [2, 3, 2, 1, 3, 1, 1, None, None, 2, 1, 1, 1], True, id="wrong 1, right"
        ),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
