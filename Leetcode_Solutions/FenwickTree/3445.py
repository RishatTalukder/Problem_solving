class FenwickTree:
    INF = float('inf')

    def __init__(self, size):
        self.size = size
        self.tree = [self.INF] * (size + 1)

    # Update the tree at index i with the minimum of current and new value
    def update(self, i, value):
        i += 1  # 1-based indexing
        while i <= self.size:
            self.tree[i] = min(self.tree[i], value)
            i += i & -i

    # Query the minimum value in range [0, i]
    def query(self, i):
        i += 1  # 1-based indexing
        result = self.INF
        while i > 0:
            result = min(result, self.tree[i])
            i -= i & -i
        return result

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # A helper class to implement Fenwick Tree (Binary Indexed Tree) for range minimum queries
        n = len(s)
        max_diff = float('-inf')  # To track the final answer

        # Try every pair of digits (a != b) from 0 to 4
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # Prefix arrays
                D = [0] * (n + 1)        # Net difference of count[a] - count[b]
                pa = [0] * (n + 1)       # Parity of count[a] (0: even, 1: odd)
                pb = [0] * (n + 1)       # Parity of count[b]
                countB = [0] * (n + 1)   # Total number of digit b up to index i

                # Build the prefix state arrays
                for i in range(1, n + 1):
                    digit = int(s[i - 1])
                    D[i] = D[i - 1] + (1 if digit == a else 0) - (1 if digit == b else 0)
                    pa[i] = (pa[i - 1] + (1 if digit == a else 0)) & 1  # Even/Odd parity
                    pb[i] = (pb[i - 1] + (1 if digit == b else 0)) & 1
                    countB[i] = countB[i - 1] + (1 if digit == b else 0)

                # 2x2 matrix of Fenwick Trees based on parity of a and b
                trees = [[FenwickTree(n + 1) for _ in range(2)] for _ in range(2)]

                for j in range(n + 1):
                    # Only update tree if the prefix ends at least k characters before current
                    if j >= k:
                        idx = j - k
                        trees[pa[idx]][pb[idx]].update(countB[idx], D[idx])

                    if j > 0:
                        need_pa = 1 - pa[j]  # We want a to be odd
                        need_pb = pb[j]      # We want b to be even

                        if countB[j] > 0:
                            # Query the best prefix value satisfying parity and b count
                            best_val = trees[need_pa][need_pb].query(countB[j] - 1)
                            if best_val != FenwickTree.INF:
                                max_diff = max(max_diff, D[j] - best_val)

        return max_diff if max_diff != float('-inf') else -1
