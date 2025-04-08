import pytest

from main import is_palidromic, palindromeIndex


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        pytest.param("bcbc", 0, id="example"),
        pytest.param("abxba", 2, id="palidromic_odd_length"),
        pytest.param("aa", -1, id="palidromic_even_length"),
        pytest.param("aax", 2, id="remove_last_char"),
        pytest.param("abcdefcba", -1, id="palidromic_to_middle"),
    ],
)
def test_palindromeIndex(s, expected, capfd):
    assert palindromeIndex(s) == expected


@pytest.mark.parametrize(
    ["s", "left", "right", "expected"],
    [
        pytest.param("bcbc", 0, 3, False, id="example"),
        pytest.param("bcbc", 1, 3, True, id="example2"),
        pytest.param("bcbc", 0, 2, True, id="example3"),
        pytest.param("axa", 0, 2, True, id="3chars"),
        pytest.param("a", 0, 0, True, id="single_char"),
        pytest.param("aa", 0, 1, True, id="double_char_expect_true"),
        pytest.param("ab", 0, 1, False, id="double_char_expect_false"),
    ],
)
def test_is_palidromic(s, left, right, expected):
    assert is_palidromic(s, left, right) == expected
