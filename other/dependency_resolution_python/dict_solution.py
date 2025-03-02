#!/usr/bin/env python
from __future__ import print_function
import pprint


class DependencyError(Exception):
    def __init__(self, data):
        self.data = data


def compute_build_order(raw_dependency):
    """
    Given a list of 2-element tuples such as [('a', 'b'), ('b': 'c')],
    where ('a', 'b') means a depends on b, generate a list of build
    order.

    :param raw_dependency: list of 2-element tuples
    :raise DependencyError: if circular dependency detected
    """
    # dependency is a dictionary where
    # - key = the name of a node (a, b, c, ...)
    # - value = a set of nodes that the key depend on.
    # That means for the input ('a', 'b'), ('a', 'c') our dict looks like:
    # {'a': set(['b', 'c']), 'b': set(), 'c': set()}
    dependency = {}
    for dependence, independence in raw_dependency:
        dependency.setdefault(dependence, set())
        dependency.setdefault(independence, set())
        dependency[dependence].add(independence)

    # Since we work with the values and items from the dependcy dict often
    # It makes sense to get them once and use them over and over
    values = dependency.viewvalues()
    items = dependency.viewitems()

    while dependency:
        independent_nodes = [k for k, v in items if not v]
        if not independent_nodes:
            raise DependencyError(dependency)

        for node in independent_nodes:
            yield node
            for v in values:
                v.discard(node)
            del dependency[node]


if __name__ == '__main__':
    raw_dependency = [
        ('a', 'b'),
        ('a', 'c'),
        ('d', 'e'),
        ('d', 'b'),
        ('b', 'e'),
        ('c', 'e'),
        ('f', 'g'),
        # ('c', 'a'),  # Uncomment to see circular depency
    ]

    try:
        print('Raw data:')
        pprint.pprint(raw_dependency)
        build_order = compute_build_order(raw_dependency)
        print('Build order:', ', '.join(build_order))
    except DependencyError as e:
        print('Circular Dependency:')
        for k, v in e.data.items():
            print('- {} depend on {}'.format(k, ', '.join(str(x) for x in v)))
