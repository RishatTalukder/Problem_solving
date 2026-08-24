import sys

path = sys.stdin.read().strip()

# 1. Pad the grid with 1s to completely remove '0 <= row < 7' checks
grid = [[1]*9 for _ in range(9)]
for r in range(1, 8):
    for c in range(1, 8):
        grid[r][c] = 0

ans = 0

# Adjusted directions for the 1-indexed internal grid
directions = [(-1,0), (1,0), (0,1), (0,-1)]

def solve():
    
    def dfs(row, col, index):
        global ans
        
        # 3. Target check (Adjusted coordinates to match 1-indexed grid: 6->7, 0->1)
        if row == 7 and col == 1:
            if index == 48:
                ans += 1
            return 

        if index == 48:
            return

        # 2. Optimized Wall Splitting (Fast Lookups with NO bounds checking)
        if grid[row-1][col] and grid[row+1][col] and not grid[row][col-1] and not grid[row][col+1]:
            return
        if grid[row][col-1] and grid[row][col+1] and not grid[row-1][col] and not grid[row+1][col]:
            return

        grid[row][col] = 1
        instruction = path[index]

        if instruction == "U":
            if not grid[row-1][col]: dfs(row-1, col, index+1)
        elif instruction == "D":
            if not grid[row+1][col]: dfs(row+1, col, index+1)
        elif instruction == "L":
            if not grid[row][col-1]: dfs(row, col-1, index+1)
        elif instruction == "R":
            if not grid[row][col+1]: dfs(row, col+1, index+1)
        elif instruction == '?':
            # Clean loop with zero extra conditional overhead
            if not grid[row-1][col]: dfs(row-1, col, index+1)
            if not grid[row+1][col]: dfs(row+1, col, index+1)
            if not grid[row][col-1]: dfs(row, col-1, index+1)
            if not grid[row][col+1]: dfs(row, col+1, index+1)

        grid[row][col] = 0

    # Start at adjusted (1,1) instead of (0,0)
    dfs(1, 1, 0)
    print(ans)

solve()
