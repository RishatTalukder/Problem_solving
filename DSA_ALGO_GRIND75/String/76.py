
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0 or t == "":
            return ""

        t_counter = Counter(t) #counting the characters of the string t
        s_counter = Counter() #counting the characters of the string s
        have , need = 0, len(t_counter) #have is the number of characters of the string t that are in the window and need is the number of characters of the string t that are required

        result, result_length = [-1, -1], float("infinity") #result is the start and end of the substring and result_length is the length of the substring

        l = 0 

        for r in range(len(s)):

            c = s[r]
            s_counter[c] += 1 #counting the characters of the string s

            if c in t_counter and s_counter[c] == t_counter[c]:
                have += 1 #increasing the number of characters of the string t that are in the window

            while have == need: #if the number of characters of the string t that are in the window is equal to the number of characters of the string t that are required

                if (r - l + 1) < result_length: #if the length of the substring is smaller then the previous found substring
                    result = [l, r] #updating the result
                    result_length = (r - l + 1) #updating the result_length

                s_counter[s[l]] -= 1 #decreasing the number of characters of the string s

                if s[l] in t_counter and s_counter[s[l]] < t_counter[s[l]]:
                    have -= 1 #decreasing the number of characters of the string t that are in the window

                l += 1 #moving the left pointer by 1

        if result[0] == -1:
            return ""

        l, r = result
        return s[l:r+1] if result_length != float("infinity") else ""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0 or t == "":
            return ""

        t_counter = Counter(t)
        temp = Counter()
        left, right = 0, 0

        result, result_length = [-1, -1], float("infinity")

        while right < len(s):
            if s[right] in t_counter:
                temp[s[right]] += 1

            if temp == t_counter: #or
                while left <= right and temp == t_counter:
                    if (right - left) < result_length:
                        result = [left, right]
                        result_length = (right - left)

                    if s[left] in t_counter:
                        temp[s[left]] -= 1

                    left += 1

            right += 1

        if result[0] == -1:
            return ""
        
        l, r = result

        return s[l:r+1] if result_length != float("infinity") else ""
