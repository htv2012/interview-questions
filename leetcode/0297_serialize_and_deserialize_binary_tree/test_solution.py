#!/usr/bin/env python3
import json

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
    "indata, expected_serialized",
    [
        pytest.param(
            "[1,2,3,null,null,4,5]",
            "[1, [2, null, null], [3, [4, null, null], [5, null, null]]]",
            id="example 1",
        ),
        pytest.param("[]", "null", id="example 2"),
        pytest.param("[5]", "[5, null, null]", id="single node"),
        pytest.param("[1, 2]", "[1, [2, null, null], null]", id="left tree only"),
        pytest.param(
            "[1, null, 2]", "[1, null, [2, null, null]]", id="right tree only"
        ),
    ],
)
def test_solution(codec, indata, expected_serialized):
    indata = json.loads(indata)
    root = tree.breadth_first_build(indata)
    actual_serialized = codec.serialize(root)
    assert actual_serialized == expected_serialized

    deserialized_root = codec.deserialize(actual_serialized)
    assert same_tree(deserialized_root, root)
