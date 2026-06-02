class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        res = 1
        arrow = points[0][1]

        for i in points[1:]:
            if i[0] > arrow:
                res += 1
                arrow = i[1]

        return res
    