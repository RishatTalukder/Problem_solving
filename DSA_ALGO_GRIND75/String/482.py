class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        first_group = n%k
        ans = []
        
        if first_group:
            ans.append(s[:first_group])
        
        for i in range(first_group, n, k):
            ans.append(s[i:i+k])
        
        return "-".join(ans)