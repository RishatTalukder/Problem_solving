class Solution:
    def maxOperations(self, nums) -> int:
        counter = []
        n = len(nums)
        while n>=2:
            summ = nums[0] + nums[1]
            
            if len(counter) == 0:
                counter.append(summ)

            else:
                if summ in counter:
                    counter.append(summ)
                
                else:
                    return len(counter)
                
              
            nums.pop(0)
            nums.pop(0)
            n -= 2

        
        return len(counter)
    

nums = [3,2,1,4,5]

sol = Solution()
print(sol.maxOperations(nums)) 