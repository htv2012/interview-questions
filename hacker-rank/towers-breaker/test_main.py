import pytest

from main import towerBreakers


@pytest.mark.parametrize(
    ["count", "height", "winner"],
    [
        pytest.param(2, 6, 2, id="example"),
        pytest.param(1, 100, 1, id="m is odd"),
        pytest.param(4, 100, 2, id="m is even"),
        pytest.param(1, 1, 2, id="m=1(1)"),
        pytest.param(100, 1, 2, id="m=1(2)"),
    ],
)
def test_towerBreakers(count, height, winner):
    assert winner == 1 or winner == 2
    assert towerBreakers(count, height) == winner
