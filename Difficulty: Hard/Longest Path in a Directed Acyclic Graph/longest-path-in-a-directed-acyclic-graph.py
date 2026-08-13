from collections import deque

class Solution:
    def maxDistance(self, V, src, edges):
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        
        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
                
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for v, w in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    
        dist = [float('-inf')] * V
        dist[src] = 0
        
        for u in topo:
            if dist[u] != float('-inf'):
                for v, w in adj[u]:
                    if dist[u] + w > dist[v]:
                        dist[v] = dist[u] + w
                        
        int_min = -2147483648
        return [int_min if x == float('-inf') else x for x in dist]