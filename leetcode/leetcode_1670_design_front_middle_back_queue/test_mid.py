from solution import NOT_FOUND


def test_pop_mid(que):
    for val in range(5):
        que.pushBack(val)
    assert len(que) == 5
    assert list(que) == [0, 1, 2, 3, 4]

    assert que.popMiddle() == 2
    assert len(que) == 4
    assert list(que) == [0, 1, 3, 4]

    assert que.popMiddle() == 1
    assert len(que) == 3
    assert list(que) == [0, 3, 4]

    assert que.popMiddle() == 3
    assert len(que) == 2
    assert list(que) == [0, 4]

    assert que.popMiddle() == 0
    assert len(que) == 1
    assert list(que) == [4]

    assert que.popMiddle() == 4
    assert len(que) == 0
    assert list(que) == []

    assert que.popMiddle() == NOT_FOUND
    assert len(que) == 0
    assert list(que) == []

    assert que.popMiddle() == NOT_FOUND
    assert len(que) == 0
    assert list(que) == []


def test_get_mid(que):
    assert que._get_mid() is None

    que.pushBack(100)
    assert que._get_mid().val == 100

    que.pushBack(200)
    assert que._get_mid().val == 100
