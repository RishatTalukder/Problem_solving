import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def builtin_sort(arr):
    arr.sort()

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start

input_sizes = [100, 500, 1000, 2000, 10000]
print("Input Size | Bubble Sort (s) | Built-in Sort (s)")
for size in input_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    bubble_time = measure_time(bubble_sort, arr)
    builtin_time = measure_time(builtin_sort, arr)
    print(f"{size:10} | {bubble_time:15.6f} | {builtin_time:15.6f}")