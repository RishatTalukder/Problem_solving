class Solution:
    def lastRemaining(self, n: int) -> int:
        left_to_right = True
        steps = 1
        begin = 1
        remaining = n
        while remaining >1:
            if left_to_right or remaining%2==1:
                begin = begin+steps
            
            remaining = remaining // 2
            steps = steps*2
            left_to_right = True if left_to_right == False else False

        return begin 


