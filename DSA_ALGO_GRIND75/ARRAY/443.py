from collections import Counter

class Solution:
    def compress(self, chars):
        left = right = 0
        length = len(chars)

        while left < length:
            right = left
            n = 0
            char_added = 0

            while right < length and chars[right] == chars[left]:
                right += 1
                n += 1

            if n > 1:
                char_removed = right - left - 1
                char_added = len(str(n))
                chars[left+1:right] = list(str(n))
                length = length - char_removed + char_added
                

            left = left + char_added + 1

        return len(chars)

    

shit = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(len(shit))

print(Solution().compress(shit))