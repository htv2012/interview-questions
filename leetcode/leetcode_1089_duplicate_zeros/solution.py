class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros_count = arr.count(0)
        size = len(arr)

        for source in range(size - 1, -1, -1):
            # Copy
            if (dest := source + zeros_count) < size:
                arr[dest] = arr[source]

            # Copy again if source contains zero
            if arr[source] == 0:
                zeros_count -= 1
                if (dest := source + zeros_count) < size:
                    arr[dest] = 0
