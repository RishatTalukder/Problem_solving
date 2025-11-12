from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1,n+1)]

        for ind, val in enumerate(ans):
            num = int(val)
            if num%3==0 and num%5==0:
                ans[ind] = "FizzBuzz"
            elif num%3==0:
                ans[ind] = "Fizz"
            elif num%5==0:
                ans[ind] = "Buzz"
            

        return ans
            
    
n = 15
print(Solution().fizzBuzz(n))