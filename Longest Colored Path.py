class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        comp_adj = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] == s[v]:
                comp_adj[u].append(v)
                comp_adj[v].append(u)

        def get_f(start):
            q = [start]
            dist = {start: 0}
            furthest = start
            max_d = 0
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                d = dist[u]
                if d > max_d:
                    max_d = d
                    furthest = u
                for v in comp_adj[u]:
                    if v not in dist:
                        dist[v] = d + 1
                        q.append(v)
            return furthest, dist, q

        visited = [False] * n
        dist_in_comp = [0] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                E1, _, comp_nodes = get_f(i)
                for node in comp_nodes:
                    visited[node] = True

                E2, dist1, _ = get_f(E1)
                _, dist2, _ = get_f(E2)

                if dist1[E2] + 1 > ans:
                    ans = dist1[E2] + 1

                for node in comp_nodes:
                    max_node_dist = dist1[node] if dist1[node] > dist2[node] else dist2[node]
                    dist_in_comp[node] = max_node_dist + 1

        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] != s[v]:
                if dist_in_comp[u] + dist_in_comp[v] > ans:
                    ans = dist_in_comp[u] + dist_in_comp[v]

        return ans
