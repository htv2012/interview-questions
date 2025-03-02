#!/usr/bin/env python3
# https://leetcode.com/problems/flatten-nested-list-iterator/description/


class NestedInteger:
    def __init__(self, value):
        if isinstance(value, list):
            self.value = [NestedInteger(e) for e in value]
        elif isinstance(value, int):
            self.value = value

    def __repr__(self):
        return f"<{self.value}>"

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.value, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.value


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = nestedList

    def next(self) -> int:
        element = self.queue.pop(0)
        return element.getInteger()

    def hasNext(self) -> bool:
        while self.queue and not self.queue[0].isInteger():
            element = self.queue.pop(0)
            self.queue[0:0] = element.getList()
        return self.queue
