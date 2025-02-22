from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        
        if k == 0:
            return True
        
        char_count = Counter(s)
        special_substrings = []
        
        i = 0
        while i < n:
            j = i
            unique_chars = set()
            valid = True
            while j < n and s[j] not in unique_chars:
                if char_count[s[j]] > 1:
                    valid = False
                    break
                unique_chars.add(s[j])
                j += 1
            
            if valid and len(unique_chars) > 0:
                special_substrings.append(j - i)
                i = j
            else:
                i += 1
        
        return len(special_substrings) >= k

# Example usage
sol = Solution()
print(sol.maxSubstringLength("abcdbaefab", 2))  # Output: True
print(sol.maxSubstringLength("cdefdc", 3))      # Output: False
print(sol.maxSubstringLength("abeabe", 0))      # Output: True
print(sol.maxSubstringLength("cjd", 3))         # Output: False