import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("9,3,4,#,#,1,#,#,2,#,6,#,#", True, id="example 1"),
        pytest.param("1,#", False, id="example 2"),
        pytest.param("9,#,#,1", False, id="example 3"),
        pytest.param("9,#,#", True, id="my 1"),
        pytest.param("#", True, id="wrong 1"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
