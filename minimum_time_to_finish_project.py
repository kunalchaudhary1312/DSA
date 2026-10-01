from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in dependencies:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()
        req_time = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                req_time[i] = duration[i]

        count = 0

        while q:
            u = q.popleft()
            count += 1

            for v in adj[u]:
                req_time[v] = max(req_time[v], req_time[u] + duration[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if count != n:
            return -1

        return max(req_time)
