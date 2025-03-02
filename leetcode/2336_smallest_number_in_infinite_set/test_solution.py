import logging

import pytest

from solution import SmallestInfiniteSet

"""
2336. Smallest Number in Infinite Set
Medium
Topics
Companies
Hint

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

 

Constraints:

    1 <= num <= 1000
    At most 1000 calls will be made in total to popSmallest and addBack.



"""


@pytest.mark.parametrize(
    "action_list, args_list, expected_list",
    [
        pytest.param(
            [
                "SmallestInfiniteSet",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
            ],
            [[], [2], [], [], [], [1], [], [], []],
            [None, None, 1, 2, 3, None, 1, 4, 5],
            id="example 1",
        ),
    ],
)
def test_solution(action_list, args_list, expected_list):
    # obj = None
    for index, (action, args, expected) in enumerate(
        zip(action_list, args_list, expected_list)
    ):
        logging.debug("============================================================")
        logging.debug(
            "Step [%d] %s(%s)", index, action, ", ".join(str(arg) for arg in args)
        )
        logging.debug("expected=%r", expected)

        if action == "SmallestInfiniteSet":
            obj = SmallestInfiniteSet(*args)
        else:
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            logging.debug("actual  =%r", expected)
            assert actual == expected
