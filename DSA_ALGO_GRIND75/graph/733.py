class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]
        if current_color == color:
            return image
        
        def dfs(sr,sc):
            if 0<=sr<=len(image)-1 and 0<=sc<=len(image[0])-1 and image[sr][sc] == current_color:
                image[sr][sc] = color
                dfs(sr+1,sc)
                dfs(sr-1,sc)
                dfs(sr,sc+1)
                dfs(sr,sc-1)

        dfs(sr,sc)
        return image
        































