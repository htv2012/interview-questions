def test_empty(empty_db):
    assert empty_db.query_frequency(1) is False

def test_add(empty_db):
    db = empty_db
    assert db.query_frequency(1) is False

    db.add(196807)
    assert db.query_frequency(1) is True

    db.add(196807)
    assert db.query_frequency(1) is False
    assert db.query_frequency(2) is True
