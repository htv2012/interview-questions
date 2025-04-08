import pytest

from main import gridChallenge


@pytest.mark.parametrize(
    ["grid", "expected"],
    [
        pytest.param(["abc", "ade", "efg"], "YES", id="example"),
        pytest.param(
            ["ebacd", "fghiij", "olmkn", "trpqs", "xywuv"], "YES", id="example2"
        ),
        pytest.param(["x"], "YES", id="single_char"),
        pytest.param(["ba", "cd"], "YES", id="2x2_expect_yes"),
        pytest.param(["za", "cd"], "NO", id="2x2_expect_no"),
    ],
)
def test_gridChallenge(grid, expected):
    assert gridChallenge(grid) == expected
