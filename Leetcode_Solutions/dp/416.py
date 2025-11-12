class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        
        target = total//2
        table = [False]*(target+1)
        table[0] = True

        for num in nums:
            for i in range(target,num-1,-1):
                table[i] = table[i] or table[i-num]

        return table[-1]