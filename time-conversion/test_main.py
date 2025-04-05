import pytest

from main import timeConversion


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        pytest.param("12:01:00PM", "12:01:00", id="example1"),
        pytest.param("12:01:00AM", "00:01:00", id="example2"),
        pytest.param("07:05:45PM", "19:05:45", id="sample0"),
    ],
)
def test_conversion(s, expected):
    assert timeConversion(s) == expected
