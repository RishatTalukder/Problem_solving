def add_binary_array(arr1, arr2):
    c = []
    carry = 0
    
    for i in range(len(arr1)-1, -1, -1):
        s = arr1[i] + arr2[i] + carry
        c.append(s % 2)
        carry = s // 2
        
    return (c + [carry])[::-1]

print(add_binary_array([1, 0, 1], [1, 1, 0]))