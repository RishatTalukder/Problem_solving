from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        arr_count = Counter(arr)

        for key, val in sorted(arr_count.items(), key=lambda x: x[1]):
            if k >= val:
                k -= val
                del arr_count[key]
            else:
                break

        return len(arr_count)