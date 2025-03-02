import logging

import pytest

from solution import LRUCache


@pytest.mark.parametrize(
    "action_list, args_list, expected_list",
    [
        pytest.param(
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
            id="example 1",
        ),
    ],
)
def test_solution(action_list, args_list, expected_list):
    obj = None
    for index, (action, args, expected) in enumerate(
        zip(action_list, args_list, expected_list)
    ):
        logging.debug("============================================================")
        logging.debug(
            "Step [%d] %s(%s)", index, action, ", ".join(str(arg) for arg in args)
        )
        logging.debug("expected=%r", expected)

        if action == "LRUCache":
            obj = LRUCache(*args)
        else:
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            logging.debug("actual=%r", actual)
            assert actual == expected
