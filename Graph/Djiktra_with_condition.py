class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Min with cost => Djikstra
        # Max number of stop => Can store it, OR each spreading step we take ALL ele in BFS
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Store best ans
        # best[node][step] = min cost using this much step to reach this node
        best = [[float('inf')] * (k+2) for _ in range(n)]
        best[src][0] = 0

        # cost, node, stops
        # Pop in heap => priotize cost first
        pq = [(0, src, 0)]

        while pq:
            cost, u, stops = heapq.heappop(pq)

            if u == dst:
                return cost
            
            # This not destination, and step > k
            if stops > k:
                continue
            
            for v,w in graph[u]:
                nc = cost + w
                if nc < best[v][stops+1]:
                    best[v][stops+1] = nc
                    heapq.heappush(pq, (nc, v, stops+1))
        
        return -1