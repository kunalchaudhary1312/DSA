class Solution:
    def largestSquare(self, mat, queries, k):
        n = len(mat)
        m = len(mat[0])

        # 2D Prefix Sum
        pref = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        # Function to get number of 1s
        # in rectangle (r1,c1) to (r2,c2)
        def get_sum(r1, c1, r2, c2):
            return (
                pref[r2 + 1][c2 + 1]
                - pref[r1][c2 + 1]
                - pref[r2 + 1][c1]
                + pref[r1][c1]
            )

        ans = []

        for r, c in queries:

            # Maximum possible radius
            high = min(
                r,
                c,
                n - 1 - r,
                m - 1 - c
            )

            low = 0
            best = -1

            while low <= high:
                mid = (low + high) // 2

                # Square coordinates
                r1 = r - mid
                c1 = c - mid
                r2 = r + mid
                c2 = c + mid

                ones = get_sum(r1, c1, r2, c2)

                if ones <= k:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # No valid 1x1 square
            if best == -1:
                ans.append(-1)
            else:
                ans.append(2 * best + 1)

        return ans
