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