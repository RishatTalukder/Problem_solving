import random

def BS(arr,target):
    left = 0
    right = len(arr) - 1
    c = 0

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid, c
        elif arr[mid] > target:
            right = mid -1

        else:
            left = mid + 1

        c+=1



    return -1

def LS(arr, target):
    c = 0
    for ind, val in enumerate(arr):
        c += 1
        if val == target:
            return ind, c 
        
    return -1



arr = list(range(1, 10000000))

target = random.choice(arr)

print('target:', target)

res, count = BS(arr, target)

print('BINARY SEARCH RESULTS')
print(res) 
print(count) 

print('LINEAR SEARCH RESULTS')
res, count = LS(arr, target)
print(res)
print(count)