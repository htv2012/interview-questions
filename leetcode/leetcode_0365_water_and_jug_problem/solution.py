class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def dfs(ax, ay) -> bool:
            nonlocal x, y, target, seen

            if (ax, ay) in seen:
                # We have been here, so return False to avoid infinite loop
                return False
            seen.add((ax, ay))

            # Success?
            if ax == target or ay == target or (ax + ay) == target:
                return True

            x_to_y_amount = min(ax, y - ay)
            y_to_x_amount = min(ay, x - ax)

            return (
                dfs(x, ay)  # fill x
                or dfs(ax, y)  # fill y
                or dfs(0, ay)  # empty x
                or dfs(ax, 0)  # empty y
                or dfs(ax - x_to_y_amount, ay + x_to_y_amount)  # pour x into y
                or dfs(ax + y_to_x_amount, ay - y_to_x_amount)  # pour y into x
            )

        seen = set()
        return dfs(0, 0)
