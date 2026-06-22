# My version 
def spiral_pos(x,y):
    if x == y == 1:
        return 1
    
    if x == y:
        return x**2-(x-1)
    
    start = (max(x,y)-1)**2 + 1
    end = max(x,y)**2

    if x > y and x%2==1:
        return start + (y-1)
    
    elif x > y and x%2==0:
        return end - (y-1)
    
    elif y > x and y%2==1:
        return end - (x-1)
    
    elif y > x and y%2==0:
        return start + (x-1)
    
n = int(input())

for _ in range(n):
    x,y = map(int, input().split(' '))
    print(spiral_pos(x,y))

# clean version
def number_spiral(x, y):
    layer = max(x, y)
    square = layer * layer

    # Bottom row
    if layer == x:
        if layer % 2 == 0:
            return square - y + 1
        return (layer - 1) ** 2 + y

    # Right column
    if layer % 2 == 0:
        return (layer - 1) ** 2 + x
    return square - x + 1


n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    print(number_spiral(x, y))