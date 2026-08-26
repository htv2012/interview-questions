import pytest

from solution import FrontMiddleBackQueue


@pytest.fixture
def que():
    return FrontMiddleBackQueue()
