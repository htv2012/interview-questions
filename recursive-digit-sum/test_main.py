import pytest

from main import superDigit

with open("input09.txt") as stream:
    s9 = stream.readline().strip()
    k9 = int(stream.readline())


@pytest.mark.parametrize(
    ["s", "k", "expected"],
    [
        pytest.param("9875", 4, 8, id="example"),
        pytest.param("46", 500, 5, id="my1"),
        pytest.param("2352342342414234134134134134134134", 9, 9, id="k=9"),
        pytest.param(s9, k9, 9, id="all_9s"),
    ],
)
def test_superDigit(s, k, expected):
    assert superDigit(s, k) == expected
