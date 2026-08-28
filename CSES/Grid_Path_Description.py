import sys

def solve():
    # Read and convert input characters into fast integers
    # U=0, D=1, L=2, R=3, ?=4
    char_map = {'U': 0, 'D': 1, 'L': 2, 'R': 3, '?': 4}
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    path = [char_map[c] for c in input_data]

    # 1. Use a flat 1D grid instead of 2D
    grid = [1] * 81
    for r in range(1, 8):
        for c in range(1, 8):
            grid[r * 9 + c] = 0

    ans = [0]  # Mutable list is faster than 'global ans' lookup

    # 1D movement offsets corresponding to map: U, D, L, R
    offsets = [-9, 9, -1, 1]

    def dfs(pos, index):
        # Target check (Row 7, Col 1 -> index 7*9 + 1 = 64)
        if pos == 64:
            if index == 48:
                ans[0] += 1
            return
        if index == 48:
            return

        # 2. Optimized Wall Splitting (1D Lookups)
        # Horizontal barrier split
        if grid[pos - 9] and grid[pos + 9] and not grid[pos - 1] and not grid[pos + 1]:
            return
        # Vertical barrier split
        if grid[pos - 1] and grid[pos + 1] and not grid[pos - 9] and not grid[pos + 9]:
            return

        # 3. Critical Diagonal Dead-End Checks
        # Top-Left split
        if not grid[pos - 10] and grid[pos - 9] and grid[pos - 1]: return
        # Top-Right split
        if not grid[pos - 8] and grid[pos - 9] and grid[pos + 1]: return
        # Bottom-Left split
        if not grid[pos + 8] and grid[pos + 9] and grid[pos - 1]: return
        # Bottom-Right split
        if not grid[pos + 10] and grid[pos + 9] and grid[pos + 1]: return

        grid[pos] = 1
        opt = path[index]

        if opt == 4:  # '?' Wildcard branch
            for dr in offsets:
                next_pos = pos + dr
                if not grid[next_pos]:
                    dfs(next_pos, index + 1)
        else:  # Specific direction branch
            next_pos = pos + offsets[opt]
            if not grid[next_pos]:
                dfs(next_pos, index + 1)

        grid[pos] = 0

    # Start position: Row 1, Col 1 -> index 1*9 + 1 = 10
    dfs(10, 0)
    print(ans[0])

if __name__ == '__main__':
    solve()
