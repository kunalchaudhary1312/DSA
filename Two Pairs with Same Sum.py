class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pair_sums = {}
        best = None

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s in pair_sums:
                    a, b = pair_sums[s]
                    if a != i and a != j and b != i and b != j:
                        if (a, b) < (i, j):
                            cand = [a, b, i, j]
                        else:
                            cand = [i, j, a, b]
                        if best is None or cand < best:
                            best = cand
                else:
                    pair_sums[s] = (i, j)

        return best if best is not None else [-1, -1, -1, -1]
