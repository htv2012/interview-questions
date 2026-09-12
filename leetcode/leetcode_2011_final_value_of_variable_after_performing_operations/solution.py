class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        value = 0
        for op in operations:
            if "++" in op:
                value += 1
            elif "--" in op:
                value -= 1
            else:
                raise ValueError(f"bad operation: {op}")

        return value
