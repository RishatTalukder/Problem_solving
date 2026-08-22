from math import floor
from sys import stdin

input = stdin.readline

n, x = map(int, input().split())

p = list(map(int, input().split()))

p.sort()

left = 0
right = n-1
count  = 0


while left <= right:
    if p[right] + p[left] <= x:
        count += 1
        right -= 1
        left += 1

    else:
        count += 1
        right -= 1



print(count)