class Solution:
    def socialNetwork(self, arr):
        res = []
        n = len(arr) + 1
        for i in range(2, n + 1):
            reachable = []
            curr = i
            dist = 0
            while curr >= 2:
                curr = arr[curr - 2]
                dist += 1
                reachable.append([i, curr, dist])
            reachable.sort(key=lambda x: x[1])
            res.extend(reachable)
        return res
