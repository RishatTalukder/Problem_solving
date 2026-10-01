import random


def merge(left : list, right: list):
    i = 0
    j = 0
    array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    array.extend(right[j:])
    array.extend(left[i:])

    return array

def merge_sort(arr:list):
    if len(arr) > 1:
        mid = len(arr)//2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

        # return left, right
    else:
        return arr

    
for i in range(10):
    res = merge_sort([random.randint(a=0,b=100) for i in range(100)])  
    print(res) 
