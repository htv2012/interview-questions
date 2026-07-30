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

    que.pushBack(100)  # que: 100
    assert que._get_mid().val == 100

    que.pushBack(200)  # que: 100 200
    assert que._get_mid().val == 100

    que.pushBack(300)  # que: 100 200 300
    assert que._get_mid().val == 200

    que.pushBack(400)  # que: 100 200 300 400
    assert que._get_mid().val == 200

    que.pushBack(500)  # que: 100 200 300 400 500
    assert que._get_mid().val == 300

    que.pushBack(600)  # que: 100 200 300 400 500 600
    assert que._get_mid().val == 300


def test_push_mid(que):
    que.pushMiddle(1)
    assert len(que) == 1
    assert list(que) == [1]

    que.pushMiddle(2)  # 2 1
    assert len(que) == 2
    assert list(que) == [2, 1]

    que.pushMiddle(3)  # 3 2 1
    assert len(que) == 3
    assert list(que) == [3, 2, 1]
