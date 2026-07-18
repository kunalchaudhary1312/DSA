class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n = len(arr)
        q = deque()
        res = []
        
        for i in range(n):
            if q and q[0] == i - k:
                q.popleft()
                
            while q and arr[q[-1]] <= arr[i]:
               q.pop()
            
            q.append(i)
            
            if i >= k -1:
                res.append(arr[q[0]])
                
                
        return res
