n = int(input())

for _ in range(n):
    a, b = map(int, input().strip().split(' '))

    if max(a,b) > min(a,b)*2:
        # print("activated")
        print("NO")
        continue

    if a == 0 == b:
        print("YES")

    elif (a==1 and b==2) or (b==1 and a==2):
        print("YES")
    
    else:
        print("NO")