import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("(let x 2 (mult x (let x 3 y 4 (add x y))))", 14, id="example 1"),
        pytest.param("(let x 3 x 2 x)", 2, id="example 2"),
        pytest.param("(let x 1 y 2 x (add x y) (add x y))", 5, id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
