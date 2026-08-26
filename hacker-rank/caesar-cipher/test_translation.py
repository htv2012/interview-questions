import pytest

from main import translate


@pytest.mark.parametrize(
    ["inchar", "k", "expected"],
    [
        ("a", 3, "d"),
        ("w", 3, "z"),
        ("x", 3, "a"),
        ("y", 3, "b"),
    ],
)
def test_translate(inchar, k, expected):
    assert translate(inchar, k) == expected
