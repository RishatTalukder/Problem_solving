a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    print(i, end=" ")

print(*[i for i in a])

print(*a, sep="\n")
