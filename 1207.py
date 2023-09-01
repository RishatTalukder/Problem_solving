from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr_hash = Counter(arr)
        if len(arr_hash.values()) == len(set(arr_hash.values())):
            return True
        
        else:
            return False 
        

arr = [1,2]

print(Solution().uniqueOccurrences(arr))