import pytest
import tree

"""
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right
side of it, return the values of the nodes you can see ordered from top
to bottom.
 

Example 1:

Input: root = [1,2,3,None,5,None,4]
Output: [1,3,4]

Example 2:

Input: root = [1,None,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

 

Constraints:

* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100


"""


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 3, None, 5, None, 4], [1, 3, 4], id="example 1"),
        pytest.param([1, None, 3], [1, 3], id="example 2"),
        pytest.param([], [], id="example 3"),
        pytest.param([1, 2, None, 3, None, 4, None], [1, 2, 3, 4], id="my 1"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
