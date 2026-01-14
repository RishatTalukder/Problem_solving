class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        
        return ans
    
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(points)-1):
            curr_x = points[i][0]
            curr_y = points[i][1]
            next_x = points[i+1][0]
            next_y = points[i+1][1]

            ans += max(abs(curr_x-next_x), abs(curr_y-next_y))

        return ans