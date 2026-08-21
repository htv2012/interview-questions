import pytest

from main import climbingLeaderboard


@pytest.mark.parametrize(
    "ranked, player, expected",
    [
        pytest.param([100, 90, 90, 80], [70, 80, 105], [4, 3, 1], id="example"),
    ],
)
def test_climb(ranked, player, expected):
    assert climbingLeaderboard(ranked, player) == expected
