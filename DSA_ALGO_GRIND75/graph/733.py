class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Given an image represented by a 2D array of integers, and the coordinates of a starting pixel (sr, sc),
        this function performs a flood fill, changing the color of the connected pixels to the specified color.

        Algorithm:
        1. Get the current color of the starting pixel.
        2. If the current color is already the specified color, return the image as it is.
        3. Define a depth-first search (DFS) function to traverse the image.
        4. In the DFS function, check if the current pixel is within the image boundaries and has the same color as the starting pixel.
        5. If the conditions are met, change the color of the current pixel to the specified color.
        6. Recursively call the DFS function for the neighboring pixels (up, down, left, right).
        7. Call the DFS function with the starting pixel coordinates.
        8. Return the modified image.

        :param image: 2D array representing the image
        :param sr: starting row index
        :param sc: starting column index
        :param color: specified color to fill
        :return: modified image after flood fill
        """
        current_color = image[sr][sc]
        if current_color == color:
            return image
        
        def dfs(sr, sc):
            if 0 <= sr <= len(image) - 1 and 0 <= sc <= len(image[0]) - 1 and image[sr][sc] == current_color:
                image[sr][sc] = color
                dfs(sr + 1, sc)
                dfs(sr - 1, sc)
                dfs(sr, sc + 1)
                dfs(sr, sc - 1)

        dfs(sr, sc)
        return image
