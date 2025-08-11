# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr) # n units
    
    # Traverse through all array elements
    for i in range(n): # 2n(n-1) unit

        # Last i elements are already in place
        for j in range(n-1): # 2(n-1) units

            if arr[j] > arr[j+1]: # c unit
                arr[j], arr[j+1] = arr[j+1], arr[j] # c unit



arr = [64, 34, 25, 12, 22, 11, 90] # 1 unit/ c

bubbleSort(arr) #

print("Sorted array:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")