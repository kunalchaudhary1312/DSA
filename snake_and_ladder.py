from collections import deque

class Solution:
    def minThrow(self, N, arr, sn):
        total = N * N

        jump = [-1] * (total + 1)

        for i in range(0, len(arr), 2):
            jump[arr[i]] = arr[i + 1]

        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        visited = [False] * (total + 1)
        q = deque()

        q.append((1, 0))
        visited[1] = True

        while q:
            pos, throws = q.popleft()

            if pos == total:
                return throws

            for dice in range(1, 7):
                nxt = pos + dice

                if nxt > total:
                    continue

                if jump[nxt] != -1:
                    nxt = jump[nxt]

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, throws + 1))

        return -1

    def minThrows(self, N, arr, sn):
        return self.minThrow(N, arr, sn)
