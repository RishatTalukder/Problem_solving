class Solution:
    def reverseVowels(self, s: str) -> str:
        a = []
        b = "aeiou"
        for i in s:
            if i.lower() in b:
                a.append(i)

        reverse_string = ""
        a = a[::-1]
        count = 0
        for i in s:
            if i.lower() in b:
                reverse_string += a[count]
                count += 1 
            else:
                reverse_string += i

        return reverse_string
    
s = "leetcode"
print(Solution().reverseVowels(s))