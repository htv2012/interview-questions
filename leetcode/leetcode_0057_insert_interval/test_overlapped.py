import pytest

from solution import is_overlapped


@pytest.mark.parametrize(
    "interval1, interval2, expected",
    [
        pytest.param([1, 5], [6, 7], False, id="no overlap"),
        pytest.param([1, 5], [5, 7], True, id="overlap"),
        pytest.param([1, 5], [2, 3], True, id="subset"),
    ],
)
def test_is_overlapped(interval1, interval2, expected):
    assert is_overlapped(interval1, interval2) is expected
    assert is_overlapped(interval2, interval1) is expected
