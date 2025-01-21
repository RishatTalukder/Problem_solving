class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,ocean):
            ocean.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dr,dc in directions:
                new_r,new_c = r+dr,c+dc

                if 0<=new_r<rows and 0<=new_c<cols and (new_r,new_c) not in ocean and heights[new_r][new_c]>=heights[r][c]:
                    dfs(new_r,new_c,ocean)


        for i in range(rows):
            dfs(i,0,pacific)
            dfs(i,cols-1,atlantic)

        for j in range(cols):
            dfs(0,j,pacific)
            dfs(rows-1,j,atlantic)


        return list(pacific & atlantic)