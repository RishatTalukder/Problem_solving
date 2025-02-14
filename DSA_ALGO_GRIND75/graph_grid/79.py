
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vigited = set()
        rows,cols = len(board), len(board[0])

        def dfs(r,c,ind):
            if ind == len(word):
                return True
            
            if (r<0 or 
                r>=rows or 
                c<0 or 
                c>=cols or 
                (r,c) in vigited or 
                board[r][c] != word[ind]):
                return False
            
            vigited.add((r,c))
            res = (
                dfs(r-1,c,ind+1) or
                dfs(r+1,c,ind+1) or
                dfs(r,c+1,ind+1) or
                dfs(r,c-1,ind+1)
            )
            vigited.remove((r,c))
            return res



        ind = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,ind):
                    return True
                
        return False
    

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c , ind):
            if ind == len(word):
                return True
            
            if not (0 <= r < rows and 0 <= c < cols) or (r,c) in visited or board[r][c] != word[ind]:
                return False

            visited.add((r,c))
            res = (
                dfs(r-1,c,ind+1) or
                dfs(r+1,c,ind+1) or
                dfs(r,c-1,ind+1) or
                dfs(r,c+1,ind+1)
            )

            visited.remove((r,c))
            return res


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
                

        return False