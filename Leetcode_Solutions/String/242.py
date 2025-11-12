from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s) #counting the characters of the string s
        t_counter = Counter(t) #counting the characters of the string t
        
        #comparing the counters, if the counters are the same then return true
        if s_counter == t_counter:
            return True
        else:
            return False
        