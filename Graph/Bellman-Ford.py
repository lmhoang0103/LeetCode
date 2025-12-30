class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Min with cost => Djikstra
        # Max number of stop => Can store it, OR each spreading step we take ALL ele in BFS
        #Bellman-Ford idea is to update min distance to each node at each step
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] != float('inf'):
                    tmp[v] = min(tmp[v], dist[u] + w)
            dist = tmp

        return -1 if dist[dst] == float('inf') else dist[dst]