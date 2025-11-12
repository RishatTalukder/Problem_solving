class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x,y = 0,0
        direction_map = {
            'N': (0,1),
            'S': (0,-1),
            'E': (1,0),
            'W': (-1,0)
        }

        for i in s:
            x += direction_map[i][0]
            y += direction_map[i][1]
        
        real_distance = abs(x) + abs(y)

        north = s.count('N')
        south = s.count('S')
        east = s.count('E')
        west = s.count('W')

        maxx_travel_direction = max(north, south, east, west)

        x_cancel = min(east, west)
        y_cancel = min(north, south)

        possible_distance_rise = 2*(x_cancel + y_cancel)

        if k >= possible_distance_rise:
            return real_distance + possible_distance_rise
        else:
            return real_distance + k
        
from collections import Counter
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        s_counter = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        x,y = 0,0
        left = 0
        right = len(s_counter) - 1

        while k > 0 and left < right:
            s_counter[left][1] += 1
            s_counter[right][1] -= 1
            k -= 1
            if s_counter[right][1] == 0:
                right -= 1

        for k,v in s_counter:
            if v%2 == 0:
                x += v
            else:
                y += v

        return x + y


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        s_counter = Counter(s)

        for k in "NS":
            if k not in s_counter:
                s_counter[k] = 0

                


        
print(Solution().maxDistance(s = "NWSE", k = 1))