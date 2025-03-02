import pytest
import tree

from solution import Codec


@pytest.mark.parametrize(
    "indata",
    [
        pytest.param([2, 1, 3], id="example 1"),
        pytest.param([], id="example 2"),
    ],
)
def test_solution(indata):
    original = tree.breadth_first_build(indata)
    codec = Codec()
    serialized = codec.serialize(original)
    assert isinstance(serialized, str)
    round_trip = codec.deserialize(serialized)

    original_inorder = [node.val for node in tree.inorder_iter(original)]
    round_trip_inorder = [node.val for node in tree.inorder_iter(round_trip)]
    assert original_inorder == round_trip_inorder
