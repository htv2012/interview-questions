VALUE_A = 1968
VALUE_B = -1155


def populate(db):
    for _ in range(3):
        db.add(VALUE_A)
    for _ in range(2):
        db.add(VALUE_B)


def test_empty(db):
    assert db.query_frequency(1) is False


def test_add(db):
    assert db.query_frequency(1) is False

    db.add(VALUE_A)
    assert db.query_frequency(1) is True

    db.add(VALUE_A)
    assert db.query_frequency(1) is False
    assert db.query_frequency(2) is True

    db.add(VALUE_B)
    assert db.query_frequency(1) is True
    assert db.query_frequency(2) is True


def test_remove(db):
    populate(db)

    assert db.query_frequency(3) is True  # There are 3 VALUE_A
    assert db.query_frequency(2) is True  # There are 2 VALUE_B
    db.remove(VALUE_B)
    assert db.query_frequency(2) is False
    assert db.query_frequency(1) is True
    assert db.query_frequency(3) is True
