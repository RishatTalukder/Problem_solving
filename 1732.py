class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        alttd = 0
        mx = 0
        for i in gain:
            alttd += i 
            mx = max(mx,alttd)
        
        return mx
    

gain = [-5,1,5,0,-7]

print(Solution().largestAltitude(gain))