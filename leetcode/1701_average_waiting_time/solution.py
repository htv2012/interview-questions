from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_times = 0
        ready_time = 0
        for order_time, cook_time in customers:
            total_wait_times += max(0, ready_time - order_time) + cook_time
            ready_time = max(ready_time, order_time) + cook_time
        return total_wait_times / len(customers)
