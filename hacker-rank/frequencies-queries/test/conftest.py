import pytest

from frequencies_queries import DB


@pytest.fixture
def empty_db():
    return DB()


@pytest.fixture
def db():
    db_obj = DB()
    for value, count in [(1, 5), (2, 3)]:
        for _ in range(count):
            db_obj.add(value)
    return db_obj