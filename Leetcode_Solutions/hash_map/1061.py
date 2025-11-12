class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if parent.get(x, x) != x:
                parent[x] = find(parent[x])
            return parent.get(x, x)

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[max(rootX, rootY)] = min(rootX, rootY)

        for a, b in zip(s1, s2):
            union(a, b)

        result = []
        for char in baseStr:
            result.append(find(char))

        return ''.join(result)


sol = Solution()
res = sol.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser")