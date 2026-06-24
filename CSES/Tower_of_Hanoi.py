res = []

def TOH(n, A,B,C):
    if (n > 0):
        TOH(n-1, A,C,B)
        res.append(f"{A} {C}")
        TOH(n-1, B, A, C)

n = int(input())

TOH(n, 1,2,3)
print(len(res))
print(*res, sep="\n")
