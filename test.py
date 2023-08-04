s = " hello    world "

new_s = s.split(' ')
new_s = new_s[::-1]

for i in new_s:
    if i:
        print(i,end=" ")
    else:
        pass