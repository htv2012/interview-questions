def countingSort(arr):
    counter = [0] * 100
    for value in arr:
        counter[value] += 1

    return counter
