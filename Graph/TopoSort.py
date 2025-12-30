class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # If already add as a visit node in order, =2, if trying to add (Means trying to add its child then itself) then visited = 1. Untouch = 0
        visited = [0] * numCourses

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        order = []

        # If try to dfs(u) => Try to add its prerequisite first: dfs(v)
        def dfs(u):
            if visited[u] == 1:
                return False # Try to add again while trying to add

            # 2 means already satisfy and in the order
            if visited[u] == 2:
                return True
            
            # If while trying to visit this, you detect a cycle => False
            # Add preq of its first
            visited[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            
            visited[u] = 2
            order.append(u)
            return True
        
        # Try to add every ele in order
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []

        return order[::-1]
    

    indegree  = [0] * numCourses

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        
        order = []
        
        # BFS
        # Idea: There HAVE to be course that don't require othercourse
        # This goes first, other that depends on this have requirement decrease by 1
        # Add course that now don't have requirement
        # After all, if there no other course => end


        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v] -=1
                if indegree[v] == 0:
                    q.append(v)
        
        if len(order) != numCourses:
            return []

        return order



#DFS
# Class containing the solution logic
class Solution:
    # Function to perform DFS
    def dfs(self, node, adj, vis, st):
        # Mark the current node as visited
        vis[node] = 1
        
        # Explore all neighbors of this node
        for it in adj[node]:
            # If the neighbor is not visited, recursively perform DFS
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)
        
        # After visiting all neighbors, push this node into the stack
        st.append(node)

    # Function to perform Topological Sort
    def topoSort(self, V, adj):
        # Create a visited array to mark visited vertices
        vis = [0] * V
        
        # List to act as stack
        st = []
        
        # Perform DFS from each unvisited vertex
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)
        
        # Reverse the stack to get topological order
        return st[::-1]
    
    # Class that contains the topological sort logic
class Solution:
    # Function to perform BFS-based topological sort
    def topologicalSort(self, V, adj):
        # Create a list to store in-degree of each vertex
        indegree = [0] * V

        # Loop over all vertices to calculate in-degree
        for i in range(V):
            # Loop through adjacent vertices
            for it in adj[i]:
                # Increase in-degree of connected vertex
                indegree[it] += 1

        # Create a queue to store vertices with in-degree zero
        from collections import deque
        q = deque()

        # Loop through all vertices
        for i in range(V):
            # If in-degree is zero, add to queue
            if indegree[i] == 0:
                q.append(i)

        # List to store topological order
        topo = []

        # Process vertices until queue is empty
        while q:
            # Remove vertex from queue
            node = q.popleft()

            # Add it to the topological order
            topo.append(node)

            # Loop through adjacent vertices of the current node
            for it in adj[node]:
                # Reduce in-degree of connected vertex
                indegree[it] -= 1
                # If in-degree becomes zero, push into queue
                if indegree[it] == 0:
                    q.append(it)

        # Return the topological ordering
        return topo