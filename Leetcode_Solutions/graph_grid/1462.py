from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adje_list = defaultdict(list)

        for i in prerequisites:
            adje_list[i[0]].append(i[1])


        memo = {}

        def dfs(node, target):
            if (node, target) in memo:
                return memo[(node, target)]

            if node == target:
                return True

            for i in adje_list[node]:
                if dfs(i, target):
                    memo[(node, target)] = True
                    return True

            memo[(node, target)] = False
            return False
        
        res = []
        for i in queries:
            res.append(dfs(i[0], i[1]))

        return res