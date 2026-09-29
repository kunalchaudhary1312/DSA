from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
        if knightPos == targetPos:
            return 0

        queue = deque([(knightPos[0], knightPos[1], 0)])
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        visited[knightPos[0]][knightPos[1]] = True

        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if nx == targetPos[0] and ny == targetPos[1]:
                    return steps + 1

                if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1
