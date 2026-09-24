"""
https://leetcode.com/problems/simple-bank-system/
"""

import pytest

from solution import Bank


@pytest.mark.parametrize(
    "actions, args_list, expected_list, end_balance",
    [
        pytest.param(
            ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
            [
                [[10, 100, 20, 50, 30]],
                [3, 10],
                [5, 1, 20],
                [5, 20],
                [3, 4, 15],
                [10, 50],
            ],
            [None, True, True, True, False, False],
            [30, 100, 10, 50, 30],
            id="Example 1",
        ),
    ],
)
def test_solution(actions, args_list, expected_list, end_balance):
    bank = Bank([])

    for action, args, expected in zip(actions, args_list, expected_list):
        if action == "Bank":
            bank = Bank(*args)
            continue

        method = getattr(bank, action)
        actual = method(*args)
        assert actual is expected

    assert bank.bal == end_balance
