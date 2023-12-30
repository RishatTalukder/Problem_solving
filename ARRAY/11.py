class Solution:
    """
    Calculate the maximum area between two bars in a histogram.
    
    Parameters:
    - height: A list of integers representing the heights of the bars in the histogram.
    
    Returns:
    - The maximum area between two bars in the histogram.
    
    Description:
    This function takes a list of integers called 'height' as input, which represents the heights of the bars in a histogram. The goal is to find the maximum area that can be formed between two bars in the histogram.
    
    The function uses the two-pointer approach to solve this problem. It initializes two pointers, 'i' and 'j', to the start and end of the 'height' list respectively. It also initializes 'max_area' to 0, which will store the maximum area found so far.
    
    The function then enters a while loop, which continues until 'i' is less than 'j'. Inside the loop, it calculates the area of the rectangle formed by the bars at positions 'i' and 'j' by taking the minimum height between them and multiplying it by the distance between them. This value is stored in 'max_temp'.
    
    The function updates 'max_area' by taking the maximum between 'max_area' and 'max_temp'. This ensures that 'max_area' always stores the maximum area found so far.
    
    Next, the function checks if the height of the bar at position 'i' is less than the height of the bar at position 'j'. If it is, 'i' is incremented by 1 to move to the next bar. Otherwise, 'j' is decremented by 1 to move to the previous bar.
    
    Once the while loop ends, the function returns the final 'max_area', which represents the maximum area between two bars in the histogram.
    
    Note: This function assumes that the input list 'height' is non-empty and contains only positive integers.
    
    Example usage:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = maxArea(height)
    print(max_area)  # Output: 49
    """
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