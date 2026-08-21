import pytest


@pytest.mark.parametrize(
    "s, t, expected",
    [
        pytest.param("abc", "ahbgdc", True, id="example 1"),
        pytest.param("axc", "ahbgdc", False, id="example 2"),
    ],
)
def test_solution(fut, s, t, expected):
    assert fut(s, t) == expected
