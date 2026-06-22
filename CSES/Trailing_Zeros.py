n = int(input())

divisor = 5

res = 0

while divisor <= n:
    res += n // divisor
    divisor = divisor*5
    # print(divisor)

print(res)