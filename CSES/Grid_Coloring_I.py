from sys import stdin
from collections import deque
input = stdin.readline

n,m = map(int, input().strip().split())

grid = []

for i in range(n):
    grid.append(
        list(input().strip())
    )

directions = [(-1,0), (0,-1)]
possible_char = {"A", "B", "C", "D"}

for i in range(n):
    for j in range(m):
        present_chars = {grid[i][j]}

        for x,y in directions:
            new_x, new_y = i+x,j+y
            if 0<=new_x<n and 0<=new_y<m:
                char = grid[new_x][new_y]
                present_chars.add(char)

        new_chars = possible_char - present_chars
        if new_chars:
            grid[i][j] = new_chars.pop()

        else:
            # print(i,j)
            print("IMPOSSIBLE")
            exit()

for i in grid:
    print("".join(i))