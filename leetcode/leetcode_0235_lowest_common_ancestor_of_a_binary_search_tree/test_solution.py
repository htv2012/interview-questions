import pytest
import tree


@pytest.mark.parametrize(
    "indata, p, q, expected",
    [
        pytest.param([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6, id="example 1"),
        pytest.param([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2, id="example 2"),
        pytest.param([2, 1], 2, 1, 2, id="example 3"),
    ],
)
def test_solution(fut, indata, p, q, expected):
    p = tree.TreeNode(p)
    q = tree.TreeNode(q)
    root = tree.breadth_first_build(indata)
    assert fut(root, p, q).val == expected
