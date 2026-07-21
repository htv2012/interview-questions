"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import contextlib
import io
import logging
from typing import Optional

import pytest
import yaml
from drawtree.drawtree import drawtree
from tree import TreeNode

logger = logging.getLogger()


def parametrize(filename, param_names):
    with open(filename) as stream:
        params_list = yaml.safe_load(stream)

    test_cases = []
    for param in params_list:
        test_id = param.pop("test_id")
        params = [param[name] for name in param_names]
        test_cases.append(pytest.param(*params, id=test_id))

    return pytest.mark.parametrize(param_names, test_cases)


def log_tree(root: Optional[TreeNode], label: str):
    if root is None:
        logger.debug("%s: (empty tree)")
        return

    with contextlib.redirect_stdout(io.StringIO()) as buf:
        drawtree(root)
    logger.debug("%s:\n%s", label, buf.getvalue())
