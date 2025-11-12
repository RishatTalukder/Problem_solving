class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find_val(ref, grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == ref:
                return 0
            grid[i][j] = ref
            return 1 + (find_val(ref, grid, i+1, j) + find_val(ref, grid, i-1, j) + find_val(ref, grid, i, j+1) + find_val(ref, grid, i, j-1))

        n = len(grid)
        ref = 2
        max_area = -1
        mp = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    k = find_val(ref, grid, i, j)
                    mp[ref] = k
                    ref += 1
                    max_area = max(max_area, k)

        mp[0] = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    sum_area = 0
                    seen = set()
                    if i > 0:
                        seen.add(grid[i-1][j])
                    if j > 0:
                        seen.add(grid[i][j-1])
                    if i < n-1:
                        seen.add(grid[i+1][j])
                    if j < n-1:
                        seen.add(grid[i][j+1])
                    for k in seen:
                        sum_area += mp.get(k, 0)
                    max_area = max(max_area, sum_area + 1)

        return max_area
    


from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Unique ID for islands (starting from 2)
        island_sizes = {}  # Dictionary to store island sizes

        # Directions for exploring adjacent cells (Up, Down, Left, Right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(i, j, id_ref):
            """DFS to find the size of an island and mark it with a unique ID."""
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = id_ref  # Mark this cell with the unique island ID
            size = 1  # This cell itself counts
            
            # Explore all 4 directions
            for di, dj in directions:
                size += dfs(i + di, j + dj, id_ref)
                
            return size
        
        # Step 1: Identify islands and store their sizes
        max_island_size = 0  # Track the largest existing island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:  # Found an unvisited island
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    max_island_size = max(max_island_size, size)
                    island_id += 1  # Move to the next unique ID
        
        # Step 2: Try flipping each 0 to find the largest possible island
        max_possible_size = max_island_size  # If no 0 exists, return max_island_size
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # Try flipping this water cell
                    seen_islands = set()
                    new_size = 1  # Include the flipped cell
                    
                    # Check all adjacent cells for island connections
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen_islands.add(grid[ni][nj])  # Collect unique island IDs
                    
                    # Sum the sizes of unique adjacent islands
                    for island in seen_islands:
                        new_size += island_sizes[island]
                    
                    # Update max_possible_size
                    max_possible_size = max(max_possible_size, new_size)
        
        return max_possible_size
