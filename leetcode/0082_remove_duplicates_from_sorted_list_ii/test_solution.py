import list_node
import pytest

"""
82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have
duplicate numbers, leaving only distinct numbers from the original
list. Return the linked list sorted as well.
 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

* The number of nodes in the list is in the range [0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.


"""


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 3, 3, 4, 4, 5], [1, 2, 5], id="example 1"),
        pytest.param([1, 1, 1, 2, 3], [2, 3], id="example 2"),
        pytest.param([], [], id="empty list"),
    ],
)
def test_solution(fut, indata, expected):
    head = list_node.ListNode.from_iterable(indata)
    actual = fut(head)
    list_node.assert_values(actual, expected)
