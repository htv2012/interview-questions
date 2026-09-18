import logging

logger = logging.getLogger()


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        size = len(arr)
        logger.debug(f"{size = }, {arr = }")
        if size < 2:
            return

        # Simulate copy to determine source and destination indices
        # for copying from right to left
        source = 0
        dest = 0
        for source, value in enumerate(arr):
            dest += 1
            if value == 0:
                dest += 1

            if dest >= size:
                dest -= 1
                break

        logger.debug(f"{source = }, {dest = }")

        # Actual copy, take care not to copy out of bound
        while source >= 0:
            # copy
            if dest < size:
                arr[dest] = arr[source]
            dest -= 1

            # copy again if source contains 0
            if arr[source] == 0:
                if dest < size:
                    arr[dest] = arr[source]
                dest -= 1

            source -= 1
