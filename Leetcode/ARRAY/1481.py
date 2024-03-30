from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        arr_count = Counter(arr)

        arr_count = sorted(arr_count.items(), key=lambda x: x[1])

        for i in range(len(arr_count)):

            k -= arr_count[i][1]

            if k < 0:
                return len(arr_count) - i
            
        return 0
