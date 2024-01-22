
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        #declaring a result list to store the start indices of the anagrams
        p_counter, s_counter = {}, {}

        #looping through the string p and counting the characters
        for i in range(len(p)):
            if p[i] not in p_counter:
                p_counter[p[i]] = 1
            else:
                p_counter[p[i]] += 1

            if s[i] not in s_counter:
                s_counter[s[i]] = 1
            else:
                s_counter[s[i]] += 1

        result = [0] if p_counter == s_counter else []

        #declaring the left and right pointers
        left = 0

        #looping through the string s
        for right in range(len(p), len(s)):
            #adding the character to the s_counter
            if s[right] not in s_counter:
                s_counter[s[right]] = 1
            else:
                s_counter[s[right]] += 1

            #removing the character from the s_counter
            s_counter[s[left]] -= 1
            if s_counter[s[left]] == 0:
                del s_counter[s[left]]
            left += 1

            #checking if the counters are the same
            if p_counter == s_counter:
                result.append(left)

        return result
    


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p) #counting the characters of the string p
        result = [] #declaring a list to store the start indices of the anagrams
        left = 0 #declaring a left pointer
        right = len(p) - 1 #declaring a right pointer

        #looping through the string s using the right pointer
        while right < len(s):
            #counting the characters from left to right
            temp = Counter(s[left:right+1])

            #comparing the counters
            if temp == counter:
                result.append(left) #adding the left pointer to the result list

            left += 1 #moving the left pointer by 1
            right += 1 #moving the right pointer by 1

        return result #returning the result list