class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn = float('inf')
        n = len(blocks)
        c = 0

        left = 0

        for right in range(n):
            if blocks[right] =='W':
                c += 1

            if right - left + 1 == k:
                mn = min(mn, c)
                if blocks[left] == 'W':
                    c -= 1
                left += 1

        return mn