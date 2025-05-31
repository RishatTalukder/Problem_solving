from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(s):
            """Convert square number to (row, col) on board."""
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square number, move count)

        while queue:
            curr, moves = queue.popleft()
            for i in range(1, 7):
                next_square = curr + i
                if next_square > n * n:
                    continue
                row, col = get_position(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # If we can't reach the end
