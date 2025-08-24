def scanner(arr, left, right):
    pivot = arr[right]
    temp = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            temp += 1
            arr[temp], arr[i] = arr[i], arr[temp]

    arr[temp+1], arr[right] = arr[right], arr[temp+1]

    return temp + 1

    



def quick_sort(arr, left,right):
    if left < right:
        pivot_ind = scanner(arr, left, right)

        quick_sort(arr,left, pivot_ind-1)
        quick_sort(arr, pivot_ind+1, right)




arr = [30,1,29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7]

left = 0
right = len(arr) - 1 

quick_sort(arr, left, right)