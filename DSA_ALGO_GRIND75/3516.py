class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_abs = abs(x-z)
        y_abs = abs(y-z)

        if x_abs == y_abs:
            return 0
        
        elif x_abs < y_abs:
            return 1

        else:
            return 2