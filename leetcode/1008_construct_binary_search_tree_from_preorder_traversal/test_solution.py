#!/usr/bin/env python3
import json

import pytest


@pytest.mark.parametrize(
    "preorder, expected",
    [
        pytest.param([8, 5, 1, 7, 10, 12], "[8,5,10,1,7,null,12]", id="example 1"),
        pytest.param([1, 3], "[1,null,3]", id="example 2"),
    ],
)
def test_solution(fut, preorder, expected):
    expected = json.loads(expected)
