class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high, total = float('inf'), float('-inf'), 0

        for x, y, l in squares:
            total += l*l
            low = min(low, y)
            high = max(high, y+l)


        target = total/2

        for i in range(60):
            mid = (high+low)/2

            curr = 0

            for x, y, l in squares:
                cur_y = max(0, min(l,mid-y))
                curr += l*cur_y

            if curr < target:
                low = mid

            else:
                high = mid

        return mid