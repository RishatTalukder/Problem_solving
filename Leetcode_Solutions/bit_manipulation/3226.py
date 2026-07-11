class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = list(bin(n)[2:])
        k = list(bin(k)[2:])

        if len(k) > len(n):
            return -1

        index = -1

        count = 0

        while index >= -min(len(n), len(k)):
            if n[index] == k[index]:
                index -= 1
                continue
            
            else:
                if n[index] == '1':
                    n[index] = '0'
                    count += 1
                else:
                    return -1   
            
            index -= 1

        while index >= -len(n):
            if n[index] == "1":
                n[index] = '0'
                count += 1
            index -= 1
            # else:
            #     return -1

        return count
