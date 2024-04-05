def solve(row,col):
    if row > col:
        if row % 2==0:
            return row*row -col + 1
        else:
            return (row-1)*(row-1)+col 
        
    else:
        if col % 2 ==0:
            return (col-1)*(col-1)+row 
        
        else:
            return col*col -row+1




test = int(input())

for _ in range(test):
    row,col = map(int,input().split())

    print(solve(row,col))
    