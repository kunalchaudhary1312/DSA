class Solution:
    def minEdgesReq(self, n, edges):
        if len(edges) < n - 1:
            return -1
            
        parent = list(range(n))
        rank = [0] * n
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                if rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False
            
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1
                
        return components - 1
