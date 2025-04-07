import pytest

from main import findZigZagSequence


@pytest.mark.parametrize(
    ["a", "n", "expected"],
    [
        pytest.param([2, 3, 5, 1, 4], 5, [1, 2, 5, 4, 3], id="example"),
        pytest.param(
            [0, 1, 2, 3, 4, 5, 6, 7, 8], 9, [0, 1, 2, 3, 8, 7, 6, 5, 4], id="case1"
        ),
    ],
)
def test_zig_zag_sequence(a, n, expected, capfd):
    findZigZagSequence(a, n)
    actual = [int(v) for v in capfd.readouterr().out.split()]
    assert actual == expected
