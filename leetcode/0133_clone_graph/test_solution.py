#!/usr/bin/env python3

import graph
import pytest


@pytest.mark.parametrize(
    "adj_list",
    [
        pytest.param([[2, 4], [1, 3], [2, 4], [1, 3]], id="example 1"),
        pytest.param([[]], id="example 2"),
        pytest.param([], id="example 3"),
    ],
)
def test_solution(fut, adj_list):
    original_graph = graph.from_adj_list(adj_list)
    cloned_graph = fut(original_graph)
    graph.assert_same_graph(cloned_graph, original_graph)


def test_none(fut):
    assert fut(None) is None


def test_simple(fut):
    original = graph.Node(1)
    cloned = fut(original)
    assert cloned is not original
    assert cloned.val == original.val
    assert cloned.neighbors == original.neighbors


def test_two_nodes(fut):
    original, friend = graph.Node(1), graph.Node(2)
    original.neighbors = [friend]
    friend.neighbors = [original]

    cloned = fut(original)

    assert cloned is not original
    assert cloned.val == original.val
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0] is not friend
    assert cloned.neighbors[0].val == friend.val
