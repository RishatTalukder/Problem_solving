class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_len = len(g)
        s_len = len(s)

        g.sort()
        s.sort()

        count = 0

        s_pointer = 0
        g_pointer = 0

        while s_pointer < s_len and g_pointer < g_len:
            if s[s_pointer] >= g[g_pointer]:
                count += 1
                s_pointer += 1
                g_pointer += 1

            else:
                s_pointer += 1


        return count