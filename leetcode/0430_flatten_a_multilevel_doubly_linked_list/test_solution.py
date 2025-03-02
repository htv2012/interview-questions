import pytest

from support import create_multi_tier, iter_list


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(
            [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12],
            [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6],
            id="example 1",
        ),
        pytest.param([1, 2, None, 3], [1, 3, 2], id="example 2"),
        pytest.param([], [], id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    head = create_multi_tier(indata)
    actual = fut(head)
    actual = [node.val for node in iter_list(actual)]
    assert actual == expected
