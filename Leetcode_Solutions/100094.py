def sublists(lst):
    n = len(lst)
    sublist = []
    summ = 0

    for start in range(n):
        for end in range(start, n):
            sublist.append(lst[start:end + 1])

    for i in sublist:
        summ += len(set(i))**2

    return summ 

original_list = [1, 2, 1]
sublists_nested = sublists(original_list)
print(sublists_nested)
