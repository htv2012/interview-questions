#!/usr/bin/env python3
"""
Binary Search Tree
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    # aliases
    @property
    def data(self):
        return self.info

    @property
    def value(self):
        return self.info

    def insert(self, value):
        if self.info == value:
            raise ValueError(f"Duplicate value: {value}")

        if value < self.info:
            if self.left is None:
                new_node = Node(value)
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                new_node = Node(value)
                self.right = new_node
            else:
                self.right.insert(value)

    @classmethod
    def from_iterable(cls, iterable):
        iterable = iter(iterable)
        root = cls(next(iterable))
        for value in iterable:
            root.insert(value)
        return root

    def __repr__(self):
        return f"{self.__class__.__name__}({self.info})"
