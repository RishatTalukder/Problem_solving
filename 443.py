from collections import Counter

class Solution:
    def compress(self, chars):

        chars_dict = Counter(chars)
        main_string = []
        for i,j in chars_dict.items():
            if j > 1:
                main_string += f"{i}{j}"

            else:
                main_string += f"{i}"

        length = len(main_string)
        return length
    

shit = ["a","a","b","b","c","c","c"]

print(Solution().compress(shit))