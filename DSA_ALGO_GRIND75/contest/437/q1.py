from collections import Counter

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        length = len(s)
        
        if k > length:
            return False
        
        for start in range(length - k + 1):
            substring = s[start:start + k]
            if len(set(substring)) == 1:
                if start > 0 and s[start - 1] == s[start]:
                    continue
                if start + k < length and s[start + k] == s[start]:
                    continue
                return True
        
        return False

# Example usage
sol = Solution()
print(sol.hasSpecialSubstring("aaabaaa", 3))  # Output: True
print(sol.hasSpecialSubstring("abc", 2))      # Output: False
print(sol.hasSpecialSubstring("h", 1))        # Output: True