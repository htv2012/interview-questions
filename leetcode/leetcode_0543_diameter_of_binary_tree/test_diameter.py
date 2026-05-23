import itertools

import pytest

from solution import breadth_first_build, diameter_of_binary_tree


def right_skewed(n: int):
    seq = itertools.chain.from_iterable(zip(range(n), itertools.repeat(None)))
    return seq


@pytest.mark.parametrize(
    "seq, expected",
    [
        pytest.param(None, 0, id="None"),
        pytest.param([1], 0, id="single node"),
        pytest.param([1, 2, 3], 2, id="3 nodes"),
        pytest.param([1, 2, 3, 4, 5], 3, id="example 1"),
        pytest.param([1, 2], 1, id="example 2, two nodes"),
        pytest.param([1, None, 2, None, 3, None, 4], 3, id="right skewed"),
        pytest.param(right_skewed(10**4), 10**4 - 1, id="long right skewed"),
    ],
)
def test_diameter(seq, expected):
    t = breadth_first_build(seq)
    assert diameter_of_binary_tree(t) == expected
