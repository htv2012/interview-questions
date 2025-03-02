#!/usr/bin/env python3
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=daily-question&envId=2024-04-08
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_count = len(students)
        counter = 0
        while counter <= students_count:
            if not students:
                return 0
            if not sandwiches:
                return len(students)

            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
                students_count = len(students)
                counter = 0
            else:
                students.append(student)
                counter += 1
        return students_count
