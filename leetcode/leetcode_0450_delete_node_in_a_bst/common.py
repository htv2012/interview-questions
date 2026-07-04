"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import pytest
import yaml


def parametrize(filename, param_names):
    with open(filename) as stream:
        params_list = yaml.safe_load(stream)

    test_cases = []
    for param in params_list:
        test_id = param.pop("test_id")
        params = [param[name] for name in param_names]
        test_cases.append(pytest.param(*params, id=test_id))

    return pytest.mark.parametrize(param_names, test_cases)
