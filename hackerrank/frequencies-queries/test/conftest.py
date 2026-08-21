import pytest

from frequencies_queries import DB


@pytest.fixture
def db():
    return DB()
