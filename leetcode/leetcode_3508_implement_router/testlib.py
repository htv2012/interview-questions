import types

import pytest


def t(tid: str, **kwargs):
    return pytest.param(types.SimpleNamespace(**kwargs), id=tid)
