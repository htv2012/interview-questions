import pytest

from solution import Solution


@pytest.fixture
def fut():
    # Function under test
    sol = Solution()
    return sol.compress
