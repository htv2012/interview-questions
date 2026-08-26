import itertools

import pytest

from solution import Node, breadth_first_iter


def breadth_first_build(seq):
    def _build(value):
        if value is None:
            return None
        return Node(value)

    if not seq:
        return None

    if not seq:
        return None

    sides = itertools.cycle(["left", "right"])
    seq = iter(seq)
    root = _build(next(seq))
    que = [root]

    for side, value in zip(sides, seq):
        node = _build(value)
        setattr(que[0], side, node)
        if node:
            que.append(node)
        if side == "right":
            que.pop(0)

    return root


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7],
            [1, None, 2, 3, None, 4, 5, 6, 7, None],
            id="example 1",
        ),
        pytest.param([], [], id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    root = breadth_first_build(indata)
    actual = fut(root)

    # Verify
    expected = (
        (val, next_val)
        for val, next_val in itertools.pairwise(expected)
        if val is not None
    )
    for node, _ in breadth_first_iter(actual):
        val, next_val = next(expected)
        assert node.val == val
        if next_val is None:
            assert node.next is None
        else:
            assert node.next.val == next_val
