n = int(input())

if n < 4:
    if n == 1:
        print(1)
    else:
        print("NO SOLUTION")

else:
    for i in range(2, n+1, 2):
        print(i, end=" ")
    for i in range(1, n+1, 2):
        print(i, end=" ")
    print()