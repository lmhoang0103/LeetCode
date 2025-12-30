# Idea:
# DFS + track discovery of nodes and the lowest discovery time reachable
# if edge (u, v) is a back edge, low(v) <= disc(u) => a bridge
# so, basically u-> v exist, then if v find a path to something lower then u, means low(v) <= disc(u) => u, v in a cycle and, also update low[u]. Otherwise this is a bride to another new cycle (means v can only reach what is > disc[u]) so we store this bridge in res?
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        time = 0
        res = []

        def dfs(u,parent):
            nonlocal time
            # Init, disc = low 
            disc[u] = low[u] = time
            time +=1

            for v in graph[u]:
                # v is parent of u => a cycle already
                if v == parent:
                    continue
                # have not discover v
                if disc[v] == -1:
                    dfs(v,u)
                    # u-v exist, therefore what v can reach u can also reach
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u,v])
                # have already discover v, then v have lower disc then u
                # low[u] = min(low[u], low[v])
                else:
                    low[u] = min(low[u], low[v])
        dfs(0,-1)

        return res