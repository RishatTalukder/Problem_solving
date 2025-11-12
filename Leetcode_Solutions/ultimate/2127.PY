class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        in_degree = defaultdict(int)
        n = len(favorite)

        for fav in favorite:
            in_degree[fav] += 1


        queue = deque([i for i in range(n) if in_degree[i] == 0])
        chain_len = [0] * n

        while queue:
            u = queue.popleft()

            v = favorite[u]
            chain_len[v] = max(chain_len[v], chain_len[u] + 1)
            in_degree[v] -= 1

            if in_degree[v] == 0:
                queue.append(v)

        visited = [False] * n
        max_cycle = 0
        two_cycle = 0

        for i in range(n):
            if not visited[i] and in_degree[i] > 0:
                cycle = 0
                u = i

                while not visited[u]:
                    visited[u] = True
                    u = favorite[u]
                    cycle += 1

                if cycle == 2:
                    a, b = i, favorite[i]
                    two_cycle += 2 + chain_len[a] + chain_len[b]
                else:
                    max_cycle = max(max_cycle, cycle)

        return max(max_cycle, two_cycle)