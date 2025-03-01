class Solution:
    def magicalString(self, n: int) -> int:
        magic_string = [1, 2, 2]

        if n <= 3:
            return magic_string[:n].count(1)
        
        pointer = 2
        cur = 1

        while len(magic_string) < n:
            magic_string.extend([cur] * magic_string[pointer])
            cur = 3 - cur
            pointer += 1

        return magic_string[:n].count(1)