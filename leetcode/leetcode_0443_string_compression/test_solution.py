import pytest


@pytest.mark.parametrize(
    "chars, expected_length, expected",
    [
        pytest.param(
            ["a", "a", "b", "b", "c", "c", "c"],
            6,
            ["a", "2", "b", "2", "c", "3"],
            id="example 1",
        ),
        pytest.param(["a"], 1, ["a"], id="example 2"),
        pytest.param(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            4,
            ["a", "b", "1", "2"],
            id="example 3",
        ),
        pytest.param(
            ["a", "a", "a", "b", "b", "a", "a"],
            6,
            ["a", "3", "b", "2", "a", "2"],
            id="wrong 1",
        ),
    ],
)
def test_solution(fut, chars, expected_length, expected):
    assert fut(chars) == expected_length
    assert chars[:expected_length] == expected
