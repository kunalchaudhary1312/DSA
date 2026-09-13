from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        def bfs(start):
            q = deque([start])
            dist = [-1] * len(adj)
            dist[start] = 0
            farthest_node = start
            max_dist = 0

            while q:
                curr = q.popleft()
                for neighbor in adj[curr]:
                    nxt = neighbor - 1 
                    if dist[nxt] == -1:
                        dist[nxt] = dist[curr] + 1
                        if dist[nxt] > max_dist:
                            max_dist = dist[nxt]
                            farthest_node = nxt
                        q.append(nxt)
            return farthest_node, max_dist

        if not adj:
            return 0

        node_a, _ = bfs(0)
        _, diameter = bfs(node_a)

        return (diameter + 1) // 2