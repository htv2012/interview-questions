import json

import pytest
from common import tree


@pytest.mark.parametrize(
    ["root", "val", "depth", "expected"],
    [
        pytest.param(
            [4, 2, 6, 3, 1, 5],
            1,
            2,
            [4, 1, 1, 2, None, None, 6, 3, 1, 5],
            id="Example 1",
        ),
        pytest.param(
            [4, 2, None, 3, 1],
            1,
            3,
            [4, 2, None, 1, 1, 3, None, None, 1],
            id="Example 2",
        ),
    ],
)
def test_solution(fut, root, val, depth, expected):
    root = tree.breadth_first_build(root)
    root2 = fut(root, val=val, depth=depth)
    actual = tree.serialize(root2)
    actual = json.loads(actual)
    assert actual == expected
