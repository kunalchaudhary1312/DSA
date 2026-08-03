class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        maxSum = [0] * n
        maxSum[0] = arr[0]
        
        for i in range(1, n):
            maxSum[i] = max(arr[i], maxSum[i-1] + arr[i])
            
        curr_sum = sum(arr[:k])
        ans = curr_sum
        
        for i in range(k, n):
            curr_sum += arr[i] - arr[i-k]
            ans = max(ans, curr_sum)
            if maxSum[i-k] > 0:
                ans = max(ans, curr_sum + maxSum[i-k])
                
        return ans