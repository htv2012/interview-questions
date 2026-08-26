import pytest
import tree


@pytest.mark.parametrize(
    "root, k, expected",
    [
        pytest.param([3, 1, 4, None, 2], 1, 1, id="example 1"),
        pytest.param([5, 3, 6, 2, 4, None, None, 1], 3, 3, id="example 2"),
    ],
)
def test_solution(fut, root, k, expected):
    root = tree.breadth_first_build(root)
    assert fut(root, k) == expected
