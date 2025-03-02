import json

import pytest

from solution import Cashier


@pytest.mark.parametrize(
    ["action_list", "params_list", "expected_list"],
    [
        pytest.param(
            '["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]',
            "[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]",
            "[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]",
            id="example 1",
        ),
        pytest.param(
            '["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]',
            "[[3,50,[1,2,3,4,5,6,7],[101,201,301,401,301,201,101]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]",
            "[null,503.00000,4020.00000,803.50000,4010.00000,4020.00000,7382.00000,2510.00000]",
            id="wrong 1",
        ),
    ],
)
def test_solution(action_list, params_list, expected_list):
    action_list = json.loads(action_list)
    params_list = json.loads(params_list)
    expected_list = json.loads(expected_list)

    obj = None
    for action, args, expected in zip(action_list, params_list, expected_list):
        if action == "Cashier":
            obj = Cashier(*args)
            continue

        method = getattr(obj, action)
        assert method is not None

        actual = method(*args)
        assert actual == expected
