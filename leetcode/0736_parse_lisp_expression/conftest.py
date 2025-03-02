import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.evaluate
