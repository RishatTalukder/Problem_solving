import math
n = int(input())

for i in range(1,n+1):
    if i == 1:
        print(0)
        continue
    comb = math.comb(i**2, 2)
    res = comb - (i-1)*(i-2)*2*2

    print(res)