import pytest

from solution import breadth_first_build, diameter, max_depth


@pytest.mark.parametrize(
    "seq, expected",
    [
        pytest.param(None, -1, id="None"),
        pytest.param([1], 0, id="single node"),
        pytest.param([1, 2, 3], 2, id="3 nodes"),
        pytest.param([1, 2, 3, 4, 5], 3, id="example 1"),
        pytest.param([1, 2], 1, id="example 2, two nodes"),
    ],
)
def test_dia(seq, expected):
    t = breadth_first_build(seq)
    assert diameter(t) == expected


@pytest.mark.parametrize(
    "seq, expected",
    [
        pytest.param(None, -1, id="None"),
        pytest.param([1], 0, id="single node"),
        pytest.param([1, 2], 1, id="two nodes"),
        pytest.param([1, 2, 3], 1, id="3 nodes"),
        pytest.param([1, 2, 3, 4, 5], 2, id="example 1"),
        pytest.param([1, None, 2, None, 3], 2, id="3-node linked list"),
    ],
)
def test_max_depth(seq, expected):
    t = breadth_first_build(seq)
    assert max_depth(t) == expected
