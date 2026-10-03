def MBA(arr: list):
    start = -1
    jump = len(arr) // 2

    while jump >= 1:
        while start + jump + 1 < len(arr) and arr[start + jump] < arr[start + jump + 1]:
            start += jump

        jump //= 2

    return start + 1
