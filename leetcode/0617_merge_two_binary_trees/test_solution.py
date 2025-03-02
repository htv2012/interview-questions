import pytest
import tree
from drawtree.drawtree import drawtree


def assert_same(actual: tree.TreeNode, expected: tree.TreeNode):
    if actual is None and expected is None:
        return
    elif actual is None or expected is None:
        raise AssertionError(f"Nodes are different: {actual=} vs {expected=}")
    assert actual.val == expected.val
    assert_same(actual.left, expected.left)
    assert_same(actual.right, expected.right)


def draw(root, label):
    print(f"\n#\n# {label}\n#")
    drawtree(root)


@pytest.mark.parametrize(
    "root1, root2, expected",
    [
        pytest.param(
            [1, 3, 2, 5],
            [2, 1, 3, None, 4, None, 7],
            [3, 4, 5, 5, 4, None, 7],
            id="example 1",
        ),
        pytest.param([1], [1, 2], [2, 2], id="example 2"),
        pytest.param([], [1, 2, 3], [1, 2, 3], id="root1 is None"),
        pytest.param([1, 2, 3], [], [1, 2, 3], id="root2 is None"),
        pytest.param([], [], [], id="both are None"),
    ],
)
def test_solution(fut, root1, root2, expected):
    root1 = tree.breadth_first_build(root1)
    root2 = tree.breadth_first_build(root2)
    expected = tree.breadth_first_build(expected)
    draw(root1, "root1")
    draw(root2, "root2")
    draw(expected, "expected")
    actual = fut(root1, root2)
    draw(actual, "actual")
    assert_same(actual, expected)
