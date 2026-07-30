"""
https://leetcode.com/problems/design-front-middle-back-queue/
"""

import pytest


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["in1"],
        kwargs["in2"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "in1, in2, expected",
    [
        tc(
            test_id="Example 1",
            in1=[
                "FrontMiddleBackQueue",
                "pushFront",
                "pushBack",
                "pushMiddle",
                "pushMiddle",
                "popFront",
                "popMiddle",
                "popMiddle",
                "popBack",
                "popFront",
            ],
            in2=[[], [1], [2], [3], [4], [], [], [], [], []],
            expected=[None, None, None, None, None, 1, 3, 4, 2, -1],
        ),
    ],
)
def test_solution(in1, in2, expected):
    #    assert fut(in1, in2) == expected
    pass
