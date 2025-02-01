class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:
            return True
        prev_even = nums[0]%2==0
        for i in range(1,n):
            parity = nums[i]%2==0

            if parity != prev_even:
                prev_even = parity
            else:
                return False

        return True