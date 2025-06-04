from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self, 
        status: List[int], 
        candies: List[int], 
        keys: List[List[int]], 
        containedBoxes: List[List[int]], 
        initialBoxes: List[int]
    ) -> int:
        
        n = len(status)
        visited = [False] * n
        have_box = [False] * n
        have_key = status[:]
        queue = deque()

        for box in initialBoxes:
            have_box[box] = True
            if have_key[box]:
                queue.append(box)

        total_candies = 0

        while queue:
            box = queue.popleft()

            if visited[box]:
                continue
            visited[box] = True
            total_candies += candies[box]

            # Gain new keys
            for key in keys[box]:
                if not have_key[key]:
                    have_key[key] = 1
                    if have_box[key] and not visited[key]:
                        queue.append(key)

            # Add new boxes
            for new_box in containedBoxes[box]:
                have_box[new_box] = True
                if have_key[new_box] and not visited[new_box]:
                    queue.append(new_box)

        return total_candies
