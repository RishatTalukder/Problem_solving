import tkinter as tk
import random
import time

# --- Bubble Sort with step-by-step swaps ---
def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a, None  # no pivot in bubble sort
    yield a, None

# --- Quick Sort with step-by-step swaps ---
def quick_sort(arr, low, high):
    if low < high:
        pivot_index, arr = yield from partition(arr, low, high)
        yield arr, pivot_index
        yield from quick_sort(arr, low, pivot_index - 1)
        yield from quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, high  # highlight pivot during swaps
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr, i + 1  # highlight final pivot position
    return i + 1, arr

# --- Drawing bars ---
def draw_bars(canvas, arr, pivot_index=None):
    canvas.delete("all")
    c_width = 1000
    c_height = 600
    bar_width = c_width / len(arr)
    max_val = max(arr)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = c_height - (val / max_val) * c_height
        x1 = (i + 1) * bar_width
        y1 = c_height

        if pivot_index is not None and i == pivot_index:
            color = "red"  # pivot
        else:
            color = "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    root.update_idletasks()

# --- Run visualization (shared) ---
def run_visualization(algorithm):
    arr = list(range(1, 150))  # adjust size for speed
    random.shuffle(arr)

    if algorithm == "bubble":
        gen = bubble_sort(arr)
    else:
        gen = quick_sort(arr, 0, len(arr) - 1)

    for step, pivot_index in gen:
        draw_bars(canvas, step, pivot_index)
        # time.sleep(0.01)  # adjust speed

# --- Tkinter UI ---
root = tk.Tk()
root.title("Sorting Visualizer")
canvas = tk.Canvas(root, width=1000, height=600, bg="white")
canvas.pack()

frame = tk.Frame(root)
frame.pack()

bubble_btn = tk.Button(frame, text="Bubble Sort", command=lambda: run_visualization("bubble"))
bubble_btn.pack(side="left", padx=10, pady=5)

quick_btn = tk.Button(frame, text="Quick Sort", command=lambda: run_visualization("quick"))
quick_btn.pack(side="left", padx=10, pady=5)

root.mainloop()
