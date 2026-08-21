import pytest


@pytest.mark.parametrize(
    ["logs", "expected"],
    [
        pytest.param(["d1/", "d2/", "../", "d21/", "./"], 2, id="Example 1"),
        pytest.param(["d1/", "d2/", "./", "d3/", "../", "d31/"], 3, id="Example 2"),
        pytest.param(["d1/", "../", "../", "../"], 0, id="Example 3"),
    ],
)
def test_solution(fut, logs, expected):
    assert fut(logs) == expected
