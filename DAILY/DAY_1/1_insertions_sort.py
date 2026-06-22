def insertion_sort(arr,n=None):
    for i, val in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = val
        

def insertion_sort_reverse(arr,n=None):
    for i, val in enumerate(arr):
        j = i - 1   
        while j >= 0 and arr[j] < val:
            arr[j+1] = arr[j]
            j = j=1
            
        arr[j+1] = val
    