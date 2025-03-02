import pytest
from common.tree import breadth_first_build


@pytest.mark.parametrize(
    ["root", "expected"],
    [
        pytest.param([1, 2, 3, 4], "1(2(4))(3)", id="Example 1"),
        pytest.param([1, 2, 3, None, 4], "1(2()(4))(3)", id="Example 2"),
        pytest.param([1], "1", id="single leaf"),
        pytest.param([1, None, 2], "1()(2)", id="no left child"),
        pytest.param([], "", id="empty"),
    ],
)
def test_solution(fut, root, expected):
    root = breadth_first_build(root)
    assert fut(root) == expected
