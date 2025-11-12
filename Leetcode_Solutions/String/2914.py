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