class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right &=(right-1)
        return right
    

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right-1

        return right