#!/usr/bin/env python3
# https://leetcode.com/problems/course-schedule/description/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = {i: set() for i in range(numCourses)}
        for course, predecessor in prerequisites:
            dependency[course].add(predecessor)

        while dependency:
            to_be_removed = {
                course
                for course, predecessors in dependency.items()
                if not predecessors
            }
            if not to_be_removed:
                return False

            for course in to_be_removed:
                del dependency[course]
            for predecessors in dependency.values():
                predecessors.difference_update(to_be_removed)
        return True
