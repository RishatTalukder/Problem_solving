class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        if num < 0:
            num = num+ (1<<32)

        
        hex_map = "0123456789abcdef"

        res = ""

        while num > 0:
            hex_index = num%16
            res += hex_map[hex_index]
            num = num//16

        return res[::-1]