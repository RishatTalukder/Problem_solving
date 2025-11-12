class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        import heapq
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find connected components
        component = {}
        comp_id = 0
        comp_map = defaultdict(list)

        visited = set()

        def bfs(start):
            nonlocal comp_id
            q = deque([start])
            visited.add(start)
            component[start] = comp_id
            comp_map[comp_id].append(start)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        component[v] = comp_id
                        comp_map[comp_id].append(v)
                        q.append(v)

        for i in range(1, c + 1):
            if i not in visited:
                bfs(i)
                comp_id += 1

        # Step 3: Create a min-heap for each component of online nodes
        comp_heap = {}   # comp_id -> min-heap of online stations
        offline = set()  # set of offline stations

        for cid, nodes in comp_map.items():
            heap = nodes[:]
            heapq.heapify(heap)
            comp_heap[cid] = heap

        # Step 4: Process queries
        res = []

        for query in queries:
            t, x = query
            if t == 1:
                if x not in offline:
                    res.append(x)
                else:
                    cid = component[x]
                    # Pop offline ones until top is online or heap is empty
                    while comp_heap[cid] and comp_heap[cid][0] in offline:
                        heapq.heappop(comp_heap[cid])
                    if not comp_heap[cid]:
                        res.append(-1)
                    else:
                        res.append(comp_heap[cid][0])
            else:
                # Mark station offline
                offline.add(x)

        return res
