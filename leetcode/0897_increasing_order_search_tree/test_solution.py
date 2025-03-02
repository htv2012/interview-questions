import pytest
import tree


def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False
    return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)


@pytest.mark.parametrize(
    ["root", "expected"],
    [
        pytest.param(
            [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9],
            [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9],
            id="Example 1",
        ),
        pytest.param([5, 1, 7], [1, None, 5, None, 7], id="Example 2"),
        pytest.param(
            [2, 1, 4, None, None, 3], [1, None, 2, None, 3, None, 4], id="wrong 1"
        ),
    ],
)
def test_solution(fut, root, expected):
    root = tree.breadth_first_build(root)
    print("\nroot:")
    tree.drawtree(root)

    expected = tree.breadth_first_build(expected)
    print("expected:")
    tree.drawtree(expected)

    actual = fut(root)
    print("actual:")
    tree.drawtree(actual)
    assert same_tree(actual, expected)
