class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        min_changes = 0
        char_stream = 0

        for i in s:
            if i == curr:
                char_stream += 1
                continue

            if char_stream%2==0:
                char_stream = 1

            else:
                char_stream = 0
                min_changes += 1

            curr = i

        return min_changes
    

class Solution:
    def minChanges(self, s: str) -> int:
        MOD = 10**9 + 7

        ans = 0

        count = 0
        cur = s[0]

        for i in s:
            if i == cur:
                count += 1
                continue

            if count%2 == 0:
                count = 1
            
            else:
                ans += 1
                count = 0

            cur = i

        return ans%MOD