from solution import NOT_FOUND


def test_init(que):
    assert len(que) == 0
    assert que.front == NOT_FOUND
    assert que.mid == NOT_FOUND
    assert que.back == NOT_FOUND
    assert que.popFront() == NOT_FOUND


def test_push_front(que):
    que.pushFront(100)
    assert len(que) == 1
    assert que.front == 100
    assert que.mid == 100
    assert que.back == 100

    que.pushFront(200)
    assert len(que) == 2
    assert que.front == 200
    assert que.mid == 100
    assert que.back == 100

    que.pushFront(300)
    assert len(que) == 3
    assert que.front == 300
    assert que.mid == 200
    assert que.back == 100

    que.pushFront(400)
    assert len(que) == 4
    assert que.front == 400
    assert que.mid == 200
    assert que.back == 100

    que.pushFront(500)
    assert len(que) == 5
    assert que.front == 500
    assert que.mid == 300
    assert que.back == 100

    assert list(que) == [500, 400, 300, 200, 100]


def test_push_back(que):
    que.pushBack(100)
    assert len(que) == 1
    assert que.front == 100
    assert que.mid == 100
    assert que.back == 100

    que.pushBack(200)
    assert len(que) == 2
    assert que.front == 100
    assert que.mid == 200
    assert que.back == 200

    que.pushBack(300)
    assert len(que) == 3
    assert que.front == 100
    assert que.mid == 200
    assert que.back == 300

    que.pushBack(400)
    assert len(que) == 4
    assert que.front == 100
    assert que.mid == 300
    assert que.back == 400


def test_pop_front(que):
    values = [100, 200, 300, 400, 500]
    for val in values:
        que.pushBack(val)
    assert list(que) == values
    assert len(que) == 5

    assert que.popFront() == 100
    assert len(que) == 4
    assert que.popFront() == 200
    assert len(que) == 3
    assert que.popFront() == 300
    assert len(que) == 2
    assert que.popFront() == 400
    assert len(que) == 1
    assert que.popFront() == 500
    assert len(que) == 0
    assert que.popFront() == NOT_FOUND
    assert len(que) == 0
    assert que.popBack() == NOT_FOUND
    assert len(que) == 0


def test_pop_back(que):
    values = [100, 200, 300, 400, 500]
    for val in values:
        que.pushBack(val)
    assert list(que) == values
    assert len(que) == 5

    assert que.popBack() == 500
    assert len(que) == 4
    assert que.popBack() == 400
    assert len(que) == 3
    assert que.popBack() == 300
    assert len(que) == 2
    assert que.popBack() == 200
    assert len(que) == 1
    assert que.popBack() == 100
    assert len(que) == 0
    assert que.popBack() == NOT_FOUND
    assert len(que) == 0
    assert que.popBack() == NOT_FOUND
    assert len(que) == 0
