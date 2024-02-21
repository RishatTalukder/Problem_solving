# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         if n == 1:
#             return 1
#         else:
#             return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


#implementaion without using math

class Solution:
    def remainingElement(self, n: int) -> int:
        if len(n) == 1:
            return n[0]
        
        else:
            return self.remainingElement((n[1::2][::-1]))

    def lastRemaining(self, n: int) -> int:
        n = self.remainingElement([i for i in range(1, n+1)])

        return n