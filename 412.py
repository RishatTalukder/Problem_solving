class Solution:
    def fizzBuzz(self, n):
        shit_list = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                shit_list.append("FizzBuzz")
            
            elif i%3==0:
                shit_list.append("Fizz")

            elif i%5==0:
                shit_list.append("Buzz")
            
            else:
                shit_list.append(str(i))
        
        return shit_list
    
n = 15
print(Solution().fizzBuzz(n))