class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        max_odd = float('-inf')
        min_even = float('inf')


        for i in c:
            if c[i]%2==0:
                min_even = min(min_even, c[i])
            else:
                max_odd = max(max_odd, c[i])


        return max_odd - min_even