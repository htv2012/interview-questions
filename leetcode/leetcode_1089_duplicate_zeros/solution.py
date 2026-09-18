import logging

logger = logging.getLogger()


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        # Count number of zeros
        zeros_count = 0
        stop = -1
        for i, num in enumerate(arr):
            if num == 0:
                zeros_count += 1
                if stop == -1:
                    stop = i

        arr_len = len(arr)
        logger.debug(f"{arr = }, {arr_len = }")
        logger.debug(f"{zeros_count = }")
        logger.debug(f"{stop = }")
        if zeros_count == 0 or zeros_count == arr_len:
            return

        src = arr_len - 1
        dest = arr_len + zeros_count

        while src >= stop:
            if dest < arr_len:
                arr[dest] = arr[src]
            logger.debug(f"copying arr[{src}]={arr[src]} to arr[{dest}], {arr = }")
            src -= 1
            dest -= 1

            if arr[src + 1] == 0 and dest < arr_len:
                arr[dest] = 0
                dest -= 1
