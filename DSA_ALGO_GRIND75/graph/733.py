class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_clr = image[sr][sc]
        if source_clr == color:
            return image
        
        def dfs(sr,sc):
            if 0<= sr < len(image) and 0<= sc < len(image[0]) and image[sr][sc] == source_clr:
                image[sr][sc] = color
                dfs(sr-1,sc)
                dfs(sr+1,sc)
                dfs(sr,sc-1)
                dfs(sr,sc+1)

        dfs(sr,sc)

        return image