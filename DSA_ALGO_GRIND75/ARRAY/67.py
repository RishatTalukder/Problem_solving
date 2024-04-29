class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:] # convert the binary string into int then add the both and then convert then added value to binary again and then as bin() function returns a str value with 0b header you have to remove the header which is why i return value[2:]