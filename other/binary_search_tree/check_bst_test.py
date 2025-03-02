#!/usr/bin/env python3
"""
Determines if a gree is a BST
"""
from bst import Node


class Checker:
    def __init__(self):
        self.previous = None
    
    def __call__(self, node):
        is_valid = (
            self.previous is None
            or self.previous.data < node.data
            or node is None
        )
        self.previous = node
        return is_valid


def inorder(root, visit):
    if root is None:
        return True
    if not inorder(root.left, visit):
        return False
    if not visit(root):
        return False
    if not inorder(root.right, visit):
        return False
    return True


def checkBST(root):
    """
    Checks a tree and returns True if it is a binary search tree (BST), which means
    
    1. The data on the left must be smaller than root
    2. The data on the right must be larger than root
    3. Same for subtrees
    """
    checker = Checker()
    is_bst = inorder(root, checker)
    return is_bst


def test_empty_node():
    assert checkBST(None) is True


def test_one_node():
    root = Node(5)
    assert checkBST(root) is True


def test_left_check_failed():
    root = Node(5)
    left = Node(10)
    root.left = left
    assert checkBST(root) is False

def test_right_check_failed():
    root = Node(5)
    child = Node(3)
    root.right = child
    assert checkBST(root) is False


def test_left_tree_has_larger_value():
    root = Node(100)
    root.left = Node(50)
    root.left.right = Node(200)

    # root.left is a valid BST...
    assert checkBST(root.left) is True
    # ... but root is not because a value in root.left (i.e. 200) is larger
    assert checkBST(root) is False


def test_right_tree_has_smaller_value():
    root = Node(100)
    root.right = Node(200)
    root.right.left = Node(50)

    # root.right is a valid BST...
    assert checkBST(root.right)
    # ... but not root, because right contains 50, which is smaller than root
    assert checkBST(root) is False
