class Solution:
    def myAtoi(self, s: str) -> int:
        new = s.strip()

        if len(new) == 0:
            return 0
        
        if new[0] == '-':
            sign = -1
            new = new[1:]
        elif new[0] == '+':
            sign = 1
            new = new[1:]

        else:
            sign = 1

        result = 0
        for i in new:
            if i.isdigit():
                result = result * 10 + int(i)
            else:
                break

        result = result * sign

        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        
        return result
    

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        sign = 1
        
        if s[0] == '+':
            sign = 1
            s = s[1:]

        elif s[0] = '-':
            sign == -1
            s = s[1:]

        num = 0
        for i in s:
            if i.isdigit():
                num = num*10+int(i)
            else:
                break

        num = sign*num

        if num < -2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31-1

        return num
    
sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -42"))