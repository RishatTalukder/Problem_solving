class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        total_area = 0
        min_x = min_y = float("inf")
        max_X = max_Y = float("-inf")
        corners = set()
        for x,y,X,Y in rectangles:
            
            for corner in {(x,y), (x,Y), (X,y), (X,Y)}:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
            
            total_area += (X-x)*(Y-y)
        

        if len(corners) != 4:
            return False

        
        for x,y in corners:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_X = max(max_X, x)
            max_Y = max(max_Y, y)
        
        if total_area==(max_X-min_x)*(max_Y-min_y):
            return True

        else:
            return False