# theories/Experimental_Complexity_Analysis

Exaperimental analysis is a method used to evaluate the performance of algorithms through empirical testing. It involves running algorithms on various inputs and measuring their execution time, memory usage, and other relevant metrics. This approach helps in understanding the practical efficiency of algorithms beyond theoretical complexity.

In python, we can use libraries like `time` for measuring execution time.

## Example of Experimental Complexity Analysis in Python

```python
import time
def example_algorithm(n):
    # A simple example algorithm that runs in O(n^2)
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

def measure_time(n):
    start_time = time.time()
    example_algorithm(n)
    end_time = time.time()
    return end_time - start_time

# Measure execution time for different input sizes
input_sizes = [10, 100, 1000, 10000, 100000, 1000000]

for size in input_sizes:
    execution_time = measure_time(size)
    print(f"Input size: {size}, Execution time: {execution_time:.6f} seconds")
```

This code defines a simple algorithm that runs in O(n^2) time complexity and measures its execution time for various input sizes. The `measure_time` function captures the time taken to execute the `example_algorithm` for different values of `n`, allowing us to analyze how the execution time scales with input size.

## Comparing Bubble Sort and Python's Built-in Sort: Experimental Complexity Analysis

Below is a Python example that compares the execution time of Bubble Sort (O(n²)) and Python's built-in `sort()` (Timsort, O(n log n)) for different input sizes.

```python
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

input_sizes = [100, 500, 1000, 2000]
print("Input Size | Bubble Sort (s) | Built-in Sort (s)")
for size in input_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    bubble_time = measure_time(bubble_sort, arr)
    builtin_time = measure_time(builtin_sort, arr)
    print(f"{size:10} | {bubble_time:15.6f} | {builtin_time:15.6f}")
```

This code generates random arrays of different sizes, sorts them using both algorithms, and prints the execution

Next: [[3_Big_O_Notation|Big O Notation]].