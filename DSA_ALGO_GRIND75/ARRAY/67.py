class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:] # convert the binary string into int then add the both and then convert then added value to binary again and then as bin() function returns a str value with 0b header you have to remove the header which is why i return value[2:]
    

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0

        # Make both strings the same length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i, j in zip(a[::-1], b[::-1]):
            summ = int(i) + int(j) + carry
            carry = summ // 2
            ans.append(str(summ % 2))

        if carry:
            ans.append('1')

        return ''.join(ans[::-1])
