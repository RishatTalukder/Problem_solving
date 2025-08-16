def counter(arr):

    hash_map = {}

    for i in arr:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1


    return hash_map


arr = [1,1,2,1,3,3,5,3,4]
 
count = counter(arr)

print(count)

from collections import Counter

print(Counter(arr))