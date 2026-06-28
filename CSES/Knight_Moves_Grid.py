from collections import deque
n = int(input())

board = [[float("inf")]*n for i in range(n)]

board[0][0] = 0

q = deque([(0,0)])

directions = [(-2,1), (-2,-1), (2,1), (2, -1), (1,2), (1,-2), (-1, 2), (-1, -2)]

while q:
    level = []

    for i in range(len(q)):
        x,y = q.popleft()
        
        for dir in directions:
            new_x, new_y = x+dir[0], y+dir[1]

            if  0<=new_x<n and 0<=new_y<n and board[new_x][new_y] == float('inf'):
                board[new_x][new_y] = 1 + board[x][y]
                level.append((new_x,new_y))

    q = deque(level)


# visited = set()

# def valid_moves(x,y):
#     if x==0 and y == 0:
#         return 0
    
#     if (x,y) in visited:
#         return board[x][y]
    
#     visited.add((x,y))

#     directions = [(-2,1), (-2,-1), (2,1), (2, -1), (1,2), (1,-2), (-1, 2), (-1, -2)]

#     moves = []

#     for dir in directions:
#         new_x, new_y = x+dir[0], y+dir[1]

#         if  0<=new_x<n and 0<=new_y<n:
#             moves.append(valid_moves(new_x, new_y))

#     min_moves = 1 + min(moves)
#     board[x][y] = min_moves
#     # visited.remove((x,y))

#     return min_moves

# valid_moves(n-1,n-1)

# for i in range(n):
#     for j in range(n):
#         if board[i][j] == float("inf"):
#             valid_moves(i,j)

for i in range(n):
    print(*board[i])

