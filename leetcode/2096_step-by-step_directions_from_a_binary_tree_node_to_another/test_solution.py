import json
import pathlib

import pytest
import tree

wrong1_path = pathlib.Path(__file__).with_name("wrong1.json")
with open(wrong1_path) as stream:
    wrong1_root = json.load(stream)


@pytest.mark.parametrize(
    "root, start_value, dest_value, expected",
    [
        pytest.param([5, 1, 2, 3, None, 6, 4], 3, 6, "UURL", id="example 1"),
        pytest.param([2, 1], 2, 1, "L", id="example 2"),
        pytest.param(wrong1_root, 29716, 54117, id="wrong 1"),
        pytest.param(range(1, 16), 11, 8, "UULL", id="11-8"),
        pytest.param(range(1, 16), 8, 12, "UUURLL", id="8-12"),
    ],
)
def test_solution(fut, root, start_value, dest_value, expected):
    root = tree.breadth_first_build(root)
    assert fut(root, start_value, dest_value) == expected
