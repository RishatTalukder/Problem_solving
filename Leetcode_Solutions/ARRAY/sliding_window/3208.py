from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        stack = []
        count = 0

        # Extend the array to simulate circular behavior
        extended_colors = colors + colors[:k-1]

        for c in extended_colors:
            if not stack or stack[-1] != c:
                stack.append(c)  # Maintain the alternating sequence
            else:
                stack = [c]  # Reset stack on consecutive same colors
            
            if len(stack) >= k:
                count += 1  # Found a valid alternating group

        return count
