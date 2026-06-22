string = input()

left = string[0]

c = 0
maxx = c

for right in string:
    if right == left:
        c += 1
        maxx = max(maxx, c)

    else:
        left = right 
        c = 1

print(maxx)