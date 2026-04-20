class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = 0
        ans = 0
        for right in range(len(colors)):
            if colors[left] != colors[right]:
                ans = max(ans, abs(left-right))

        for left in range(len(colors)):
            if colors[left] != colors[right]:
                ans = max(ans, abs(left-right))


        return ans