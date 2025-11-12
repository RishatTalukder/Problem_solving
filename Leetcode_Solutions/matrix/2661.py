class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        positions = {}

        for row in range(rows):
            for col in range(cols):
                positions[mat[row][col]] = (row, col)
            
        row_count = [cols]*rows
        col_count = [rows]*cols

        for ind, val in enumerate(arr):
            row, col = positions[val]
            row_count[row] -= 1
            col_count[col] -= 1

            if row_count[row] == 0 or col_count[col] == 0:
                return ind
            
        return -1