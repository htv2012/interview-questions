import pytest

from main import breakingRecords


@pytest.mark.parametrize(
    ["scores", "expected"],
    [
        pytest.param([12, 24, 10, 24], (1, 1), id="first example"),
        pytest.param([10, 5, 20, 20, 4, 5, 2, 25, 1], (2, 4), id="sample 0"),
        pytest.param([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], (4, 0), id="sample 2"),
        pytest.param([1, 2, 3], (2, 0), id="all increasing"),
        pytest.param([1, 1, 1, 1], (0, 0), id="no breaking"),
    ],
)
def test_record(scores, expected):
    assert breakingRecords(scores) == expected
