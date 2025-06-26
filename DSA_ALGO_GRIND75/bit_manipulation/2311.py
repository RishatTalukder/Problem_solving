class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sm = 0              # current value of the selected bits
        cnt = 0             # count of characters in valid subsequence
        bits = k.bit_length()  # max number of bits needed to represent k

        for i, ch in enumerate(s[::-1]):  # reverse iterate so LSB comes first
            if ch == "1":
                if i < bits and sm + (1 << i) <= k:
                    sm += 1 << i
                    cnt += 1
            else:
                cnt += 1

        return cnt
