
import string 
from collections import Counter
from sys import stdin

val = stdin.readline().strip()

val_count = Counter(val)
n = len(val)
# print(val_count.most_common(1))

most_common_char = val_count.most_common(1)[0][0]

if val_count[most_common_char] > (n+1)//2:
    print(-1)
    exit()

prev = None
remaining = n
ans = []
chars = sorted(val_count.keys())

for i in range(n):
    for char in chars:
        if val_count[char] == 0:
            continue

        if char == prev:
            continue

        val_count[char] -= 1
        remaining = remaining - 1

        if char == most_common_char:
            most_common_char = val_count.most_common(1)[0][0]

        if val_count[most_common_char] <= (remaining + 1)//2:
            ans.append(char)
            prev = char
            break
            
        else:
            val_count[char] += 1
            remaining += 1

print(*ans, sep='')


