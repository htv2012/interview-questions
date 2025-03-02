#!/usr/bin/env python3
"""
Binary Search Tree: lowest common ancestor finder
"""
import pytest

from bst import Node


def path_to(root, value):
    """ Finds path from root to node containing value """
    if root is None:
        raise ValueError(f"Cannot find {value}")

    path = [root]
    if value < root.info:
        return path + path_to(root.left, value)
    elif value > root.info:
        return path + path_to(root.right, value)
    else:
        return path


def lca(root, v1, v2):
    path1 = path_to(root, v1)
    path2 = path_to(root, v2)

    lca_value = None
    for n1, n2 in zip(path1, path2):
        if n1.info != n2.info:
            break
        lca_value = n1
    return lca_value


def test_lca_simple_tree():
    root = Node.from_iterable([2, 1, 3])
    assert lca(root, 1, 3).info == 2
    assert lca(root, 2, 3).info == 2
    assert lca(root, 2, 1).info == 2

def test_lca_3_levels():
    #       4
    #     /   \
    #    2      7
    #  /  \   /
    # 1    3 6
    root = Node.from_iterable([4, 2, 3, 1, 7, 6])
    assert lca(root, 1, 7).info == 4
    assert lca(root, 1, 2).info == 2
    assert lca(root, 1, 3).info == 2
    assert lca(root, 1, 4).info == 4
    assert lca(root, 1, 6).info == 4
    assert lca(root, 1, 6).info == 4

    assert lca(root, 2, 1).info == 2
    assert lca(root, 2, 3).info == 2
    assert lca(root, 2, 4).info == 4
    assert lca(root, 2, 6).info == 4
    assert lca(root, 2, 7).info == 4

    assert lca(root, 4, 4).info == 4

def test_lca_multiple_levels():
    # 10 - 20 - 30 - 40 - 50 - 60 - 70 - 75
    #                                |-- 65
    root = Node.from_iterable([10, 20, 30, 40, 50, 60, 70, 65, 75])
    assert lca(root, 65, 75).info == 70
    


def test_path1():
    root = Node.from_iterable([2, 1, 3])
    assert path_to(root, 2) == [root]
    assert path_to(root, 1) == [root, root.left]
    assert path_to(root, 3) == [root, root.right]

def test_path1_not_found():
    root = Node.from_iterable([2, 1, 3])
    with pytest.raises(ValueError):
        assert path_to(root, 7)

def test_path2():
    #       4
    #     /   \
    #    2      7
    #  /  \   /
    # 1    3 6
    root = Node.from_iterable([4, 2, 3, 1, 7, 6])
    assert path_to(root, 4) == [root]
    assert path_to(root, 2) == [root, root.left]
    assert path_to(root, 3) == [root, root.left, root.left.right]
    assert path_to(root, 1) == [root, root.left, root.left.left]
    assert path_to(root, 7) == [root, root.right]
    assert path_to(root, 6) == [root, root.right, root.right.left]
    
    