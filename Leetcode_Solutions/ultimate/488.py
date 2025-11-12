from functools import cache

class Solution:
    def compress(self, board: str) -> str:
        """
        Removes consecutive groups of 3 or more balls from the board.
        """
        stack = []
        
        for c in board:
            # If the last group in stack has 3+ balls, remove it
            if stack and stack[-1][1] >= 3:
                stack.pop()
            
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1  # Increment count of last group
            else:
                stack.append([c, 1])  # Create a new group
        
        # Final check for removal of last group
        if stack and stack[-1][1] >= 3:
            stack.pop()

        return "".join(c * count for c, count in stack)

    def findMinStep(self, board: str, hand: str) -> int:
        """
        Returns the minimum number of balls needed to clear the board.
        If it's not possible, return -1.
        """
        n = len(hand)
        hand = "".join(sorted(hand))  # Sorting helps in pruning duplicate states

        @cache
        def dfs(board: str, hand: str) -> int:
            """
            Recursive DFS with memoization to find the minimum steps.
            """
            board = self.compress(board)  # Remove groups of 3 or more
            if not board:
                return n - len(hand)  # Success case: all balls removed
            
            if not hand:
                return float("inf")  # No more moves possible

            min_moves = float("inf")

            # Try inserting each ball in hand at every position in board
            for i, ball in enumerate(hand):
                if i > 0 and hand[i] == hand[i - 1]:  
                    continue  # Skip duplicate insertions for the same color
                
                for j in range(len(board) + 1):
                    # Smart insertion:
                    # Insert before a matching ball OR between two matching balls
                    if j > 0 and board[j - 1] == ball:
                        min_moves = min(min_moves, dfs(board[:j] + ball + board[j:], hand[:i] + hand[i+1:]))

                    elif j < len(board) and j > 0 and board[j - 1] == board[j] and board[j] != ball:
                        min_moves = min(min_moves, dfs(board[:j] + ball + board[j:], hand[:i] + hand[i+1:]))

            return min_moves
        
        result = dfs(board, hand)
        return result if result != float("inf") else -1  # Return -1 if no valid solution
