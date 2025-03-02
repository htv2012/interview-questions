import json

import nary_tree
import pytest


@pytest.mark.parametrize(
    ["root", "expected"],
    [
        pytest.param(
            [1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]], id="Example 1"
        ),
        pytest.param(
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
            [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
            id="Example 2",
        ),
    ],
)
def test_solution(fut, root, expected):
    root = json.dumps(root)
    root = nary_tree.deserialize(root)
    assert fut(root) == expected
