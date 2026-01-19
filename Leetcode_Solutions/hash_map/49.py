from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[tuple(sorted(s))].append(s)

        return list(groups.values())
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in str:
            hashmap[tuple(sorted(i))].append(i)

        return list(hashmap.values())