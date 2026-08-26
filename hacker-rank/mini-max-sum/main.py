def miniMaxSum(arr):
    largest, smallest = arr[0], arr[0]
    total = 0
    for value in arr:
        largest = max(largest, value)
        smallest = min(smallest, value)
        total += value
    print(total - largest, total - smallest)
