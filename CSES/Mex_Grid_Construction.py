n = int(input())

grid = [[0]*n for _ in range(n)]

grid[0] = [i for i in range(n)]
up = [{i} for i in range(n)]

# left = set()

for i in range(1,n):
    left = set()
    # print(*up)
    
    for j in range(n):
        val = 0
        while val in left or val in up[j]:
            val += 1
        grid[i][j] = val
        left.add(val)
        up[j].add(val)

    # print(*left)


# for j in range(n):
#     up = grid[0][j]
#     for i in range(1,j):
#         if i != j:
#             if j%2==0:
#                 grid[i][j] = up+1
#                 up += 1
#             else:
#                 grid[i][j] = up -1
#                 up -= 1        
#         else:
#             break

# for i in range(n):
#     for j in range(i):
#         grid[i][j] = grid[j][i]




for i in range(n):
    print(*grid[i])