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
    
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        high = float('-inf')
        low = float('inf')

        total = 0

        for x,y, l in squares:
            total += l*l
            high = max(high, y+l)
            low = min(low, y)


        target = total/2

        eps = 10**-6

        while (high-low) > eps:
            mid = (high+low)/2

            under = 0

            for x,y,l in squares:
                height = max(0, min(l, mid-y))
                under += height*l

            if under < target:
                low = mid

            else:
                high = mid

        return mid