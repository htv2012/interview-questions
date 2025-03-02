import pathlib

import pytest


@pytest.fixture(autouse=True)
def rmdb():
    db_path = pathlib.Path("/tmp/movie.sqlite3")
    db_path.unlink(missing_ok=True)
