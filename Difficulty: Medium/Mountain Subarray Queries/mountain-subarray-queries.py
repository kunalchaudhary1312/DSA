class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        if not n:
            return []
            
        next_inc = [0] * n
        next_dec = [0] * n
        
        next_inc[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                next_inc[i] = next_inc[i + 1]
            else:
                next_inc[i] = i
                
        next_dec[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                next_dec[i] = next_dec[i + 1]
            else:
                next_dec[i] = i
                
        res = []
        for l, r in queries:
            p = next_inc[l]
            if p >= r:
                res.append(True)
            else:
                res.append(next_dec[p] >= r)
                
        return res