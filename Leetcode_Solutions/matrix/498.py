
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        parity = True

        res = []

        for s in range(row + col - 1):
            if parity:
                r = min(s, row - 1)
                c = s - r
                while r >= 0 and c < col:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(s, col - 1)
                r = s - c
                while c >= 0 and r < row:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
            parity = not parity

        return res