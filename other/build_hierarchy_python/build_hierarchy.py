#!/usr/bin/env python

""" 
@file build_tree.py

# Problem

Given a list of tuples, each tuple is a pair of parent/child strings.
Write a function `printTree(input)` to print out the relationships
between the parent/children.

# Example input

    input = []
    input.append(("animal", "mammal")) 
    input.append(("animal", "bird")) 
    input.append(("lifeform", "animal")) 
    input.append(("cat", "lion")) 
    input.append(("mammal", "cat")) 
    input.append(("animal", "fish"))

# Expected output

    line 1: lifeform 
    line2:    animal 
    line 3:     mammal 
    line 4:       cat 
    line 5:         lion 
    line 6:     bird 
    line 7:     fish

"""

import collections

def print_node(tree, node, level=0):
    """
    Prints each node, and children if present.

    @param tree The tree which stores the relationship between parent
           and children
    @param node The name of the current node
    @param level The level of indentation. The first time called, level
           should be zero.
    """
    print '  ' * level, '-', 
    print node

    if not tree.has_key(node): return
    for child in tree[node]:
        print_node(tree, child, level + 1)

def print_tree(input):
    """
    Given a list of tuples specifying parent/child relationship, print
    the list in hierachical format.

    @param input The list of tuples
    """
    tree = collections.defaultdict(list)
    children = set()

    for parent, child in input:
        children.add(child)
        tree[parent].append(child)

    for node in tree:
        if node not in children:
            print_node(tree, node)

def main():
    input = []
    input.append(("animal", "mammal")) 
    input.append(("animal", "bird")) 
    input.append(("lifeform", "animal")) 
    input.append(("cat", "lion")) 
    input.append(("mammal", "cat")) 
    input.append(("animal", "fish"))

    input.append(('Novels', 'Divergent'))
    input.append(('Divergent', 'Four'))
    input.append(('Divergent', 'Trish'))
    input.append(('Novels', 'Hunger Games'))
    input.append(('Hunger Games', 'Katniss'))
    input.append(('Hunger Games', 'Peeta'))

    print_tree(input)

if __name__ == '__main__':
    main()