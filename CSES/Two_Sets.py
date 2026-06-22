n = int(input())

nums = list(range(1, n+1))

total = sum(nums)

possible = not total%2

if not possible:
    print("NO")
    exit()

set1 = []
set2 = []

need = total // 2

for i in nums[::-1]:
    if i <= need:
        set1.append(i)
        need -= i
    
    else:
        set2.append(i)


print("YES")
print(len(set1))
print(*set1)
print(len(set2))
print(*set2)