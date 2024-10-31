i = int(input())

count = 0

for _ in range(i):
    s = list(map(int, input().split()))
    if sum(s)>=2:
        count += 1

print(count)