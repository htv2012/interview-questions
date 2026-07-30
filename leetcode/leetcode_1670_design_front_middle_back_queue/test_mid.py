from solution import NOT_FOUND


def test_mid(que):
    assert que.popMiddle() == NOT_FOUND

    que.pushFront(100)
    assert que.popMiddle() == 100


def test_pop_mid2(que):
    for val in [100, 200]:
        que.pushBack(val)
    assert len(que) == 2
    assert list(que) == [100, 200]

    assert que.popMiddle() == 200
    assert len(que) == 1
    assert list(que) == [100]
