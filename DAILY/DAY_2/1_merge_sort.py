def merge(arr, l, m, r):
    left = arr[l:m]
    right = arr[m:r]
    
    i = 0
    j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1
        
    if i < len(left):
        arr[k:r] = left[i:]
        
    if j < len(right):
        arr[k:r] = right[j:]
        
    return arr

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

import random

arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
merge_sort(arr, 0, len(arr)-1)
print(arr)