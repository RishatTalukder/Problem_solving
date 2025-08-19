class Solution:
    def total_subs(self,n):
        return (n * (n + 1)) // 2


    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                total += self.total_subs(count)
                count = 0
        total += self.total_subs(count)

        return total