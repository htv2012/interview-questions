from typing import List


def busy_student(start_time: List[int], end_time: List[int], query_time: int) -> int:
    return sum(1 for a, b in zip(start_time, end_time) if a <= query_time <= b)


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        return busy_student(startTime, endTime, queryTime)
