import pytest

from solution import Router

PACKETS = [
    (1, 2, 5),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 1, 8),
    (5, 2, 9),
]


@pytest.fixture
def router() -> Router:
    r = Router(7)
    for packet in PACKETS:
        r.addPacket(*packet)
    return r
