from itertools import permutations 

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        for i in range(1, len(tiles) + 1):
            for perm in permutations(tiles, i):
                s.add("".join(perm))

        return len(s)
    

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq_map = Counter(tiles)

        def backtrack(freq_map):
            total = 0

            for char in freq_map:
                if freq_map[char] > 0:
                    # Consider the current character
                    total += 1

                    # Use the character and reduce its count
                    freq_map[char] -= 1

                    # Continue building sequences
                    total += backtrack(freq_map)

                    # Backtrack: restore the count
                    freq_map[char] += 1

            return total

        return backtrack(freq_map)
