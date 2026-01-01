class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)

        for i in prerequisites:
            adj_list[i[0]].append(i[1])

        memo={}

        def dfs(node, target):
            if (node, target) in memo:
                return memo[(node, target)]

            if node == target:
                return True

            for i in adj_list[node]:
                if dfs(i, target):
                    memo[(i, target)] = True
                    return True

            memo[(node,target)] = False

            return False


        res = []

        for i in queries:
            res.append(dfs(i[0], i[1]))


        return res