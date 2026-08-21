import pytest
import tree


@pytest.mark.parametrize(
    "inorder, postorder, expected",
    [
        pytest.param(
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3],
            [3, 9, 20, None, None, 15, 7],
            id="example 1",
        ),
        pytest.param([-1], [-1], [-1], id="example 2"),
        pytest.param([1, 2, 3], [1, 3, 2], [2, 1, 3], id="my 1"),
    ],
)
def test_solution(fut, inorder, postorder, expected):
    expected = tree.breadth_first_build(expected)
    actual = fut(inorder, postorder)

    expected_bread_first = tree.breadth_first_iter(expected)
    actual_bread_first = tree.breadth_first_iter(actual)

    for (actual_node, actual_level), (expected_node, expected_level) in zip(
        actual_bread_first, expected_bread_first
    ):
        assert actual_level == expected_level
        assert actual_node.val == expected_node.val
