class Solution:
    def reverseWords(self, s: str):

        new_s = s.split(' ')
        new_s = new_s[::-1]
        shit_words = ""
        for i in new_s:
            if i:
                shit_words += f"{i} "
            else:
                pass

        
        return shit_words.strip()
    

s = "a good   example"
print(Solution().reverseWords(s))