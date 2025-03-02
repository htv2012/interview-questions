import pytest
import tree


@pytest.mark.parametrize(
    "root, expected",
    [
        pytest.param([1, 2, 3, None, 5], ["1->2->5", "1->3"], id="example 1"),
        pytest.param([1], ["1"], id="example 1"),
    ],
)
def test_solution(fut, root, expected):
    root = tree.breadth_first_build(root)
    assert set(fut(root)) == set(expected)
