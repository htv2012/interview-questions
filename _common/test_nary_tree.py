import nary_tree


def test_deserialize_empty():
    assert nary_tree.deserialize("[]") is None


def test_deserialize_multi_levels():
    root = nary_tree.deserialize(
        "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]"
    )
    print("\nroot:")
    nary_tree.show(root)
    assert root is not None
    assert [node.val for node in root.children] == [2, 3, 4, 5]

    n2 = root.children[0]
    assert n2.val == 2
    assert n2.children is None

    n3 = root.children[1]
    assert n3.val == 3
    assert [node.val for node in n3.children] == [6, 7]
