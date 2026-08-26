import pytest

from solution import Solution


@pytest.fixture(scope="session")
def fut():
    # Function under test
    sol = Solution()
    return sol.countAndSay
