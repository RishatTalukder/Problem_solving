class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) -1
        max_area = 0
        
        while i < j:
            max_temp = min(height[i],height[j])*(j-i)
            max_area = max(max_area,max_temp)
            if height[i]<height[j]:
                i += 1
            
            else:
                j -= 1
            
        return max_area
    

a = [1,1]
print(Solution().maxArea(a))