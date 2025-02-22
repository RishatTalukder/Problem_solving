import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0

        for house in houses:
            radius = float('inf')
            index = bisect.bisect_left(heaters,house)

            if index>0:
                radius = min(radius,house-heaters[index-1])

            if index<len(heaters):
                radius = min(radius,heaters[index]-house)

            ans = max(ans,radius)

        return ans