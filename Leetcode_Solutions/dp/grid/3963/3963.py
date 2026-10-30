class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        first_row = ['.'*n]

        other_rows = ['#'*(n-1) + '.']*(m-1)

        return first_row + other_rows