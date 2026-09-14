from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        if not mat or not mat[0]:
            return -1

        n = len(mat)
        m = len(mat[0])
        safe = [[True] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = False

        q = deque()
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            if safe[i][0]:
                q.append((i, 0, 1))
                visited[i][0] = True

        while q:
            r, c, d = q.popleft()

            if c == m - 1:
                return d

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dx, c + dy

                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and safe[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

        return -1
