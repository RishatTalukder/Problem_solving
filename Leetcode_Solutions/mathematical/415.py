import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(50000)
        return str(int(num1)+int(num2))
    


class Solution: 
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0

        for i in num1:
            n1 = n1*10 + ord(i) - ord('0')

        n2 = 0
        for i in num2:
            n2 = n2*10 + ord(i) - ord('0')

        res = n1+n2
        
        res_str = ''

        if res == 0:
            return '0'
        else:
            while res != 0:
                mod = res%10
                res_str += str(mod)
                res = res//10
            
        return res_str[::-1]
    

print(Solution().addStrings("0","0"))