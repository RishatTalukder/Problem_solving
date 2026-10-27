class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m == 1:
            return ['.'*n]

        if n == 1:
            return ['.']*m


        first_row = ['.'*n]

        other_rows = ['#'*(n-1) + '.']*(m-1)

        return first_row + other_rows