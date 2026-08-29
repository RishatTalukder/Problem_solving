from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or (len(strs) == 1 and not(strs[0])):
            return ''

        min_len = min(len(i) for i in strs)

        print(min_len)

        match = True

        count = 0

        for i in range(min_len):
            prev = strs[0][i]

            for j in strs[1:]:
                if j[i] != prev:
                    match = False

            if match == False:
                break

            count += 1

        return strs[0][:count]
