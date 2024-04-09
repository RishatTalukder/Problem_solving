class Solution:
    def trap(self, height) -> int:
        maxleft = [0] * len(height)  # Initialize an array to store the maximum height to the left of each element
        maxright = [0] * len(height)  # Initialize an array to store the maximum height to the right of each element

        for i in range(1, len(height)):
            maxleft[i] = max(maxleft[i - 1], height[i - 1])  # Calculate the maximum height to the left of each element

        for i in range(len(height) - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], height[i + 1])  # Calculate the maximum height to the right of each element

        res = 0
        for i in range(len(height)):
            if min(maxleft[i], maxright[i]) > height[i]:  # Check if there is a trap at the current element
                res += min(maxleft[i], maxright[i]) - height[i]  # Calculate the amount of water trapped at the current element

        return res  # Return the total amount of water trapped

